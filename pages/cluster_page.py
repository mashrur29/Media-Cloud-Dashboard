import streamlit as st
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO
from helpers import get_data, group_colors, remove_stopwords
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud

data = get_data()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

sidebar_logo = 'assets/mediacloud-logo-black-2x.png'
main_body_logo = 'assets/mediacloud-logo-black-2x.png'
st.logo(sidebar_logo, icon_image=main_body_logo)

def get_cluster_data(cluster_name, selected_week):
    for cluster in data[selected_week]:
        if cluster['name'] == cluster_name:
            return cluster
    return None

@st.cache_data
def create_pie_chart(cluster, selected_groups):
    all_groups = list(group_colors.keys())
    if len(selected_groups) == len(cluster["distribution"]):
        filtered_distribution = cluster["distribution"]
    else:
        filtered_distribution = {
            k: v if k in selected_groups else 0
            for k, v in cluster["distribution"].items()
        }
        other_count = cluster["article_counts"] - sum(filtered_distribution.values())
        filtered_distribution["Other"] = other_count

    filtered_distribution = {k: v for k, v in filtered_distribution.items() if v > 0}
    filtered_distribution_all = cluster["distribution"]

    labels = [group for group in all_groups if group in filtered_distribution_all]
    values = [filtered_distribution_all[group] for group in labels]
    colors = [group_colors[label] if label in filtered_distribution else '#5C6068' for label in labels]

    # colors = [group_colors[label] for label in labels]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker=dict(colors=colors), sort=False)])
    fig.update_traces(textinfo='percent+label')

    return fig

@st.cache_data
def display_sample_articles(cluster, selected_groups):
    filtered_articles = [article for article in cluster["articles"] if article["collection"] in selected_groups]
    sampled_articles = filtered_articles[:5]  # Sample 5 articles
    articles_list = [f"- [{article['title']}]({article['url']}) | {article['collection'].title()}" for article in
                     sampled_articles]
    return articles_list


@st.cache_data
def fetch_image(url):
    return Image.open(BytesIO(requests.get(url).content))


def display_sample_images(cluster, selected_groups):
    if "Other" in selected_groups:
        filtered_articles = [article for article in cluster["articles"] if article["collection"] not in selected_groups]
    else:
        filtered_articles = [article for article in cluster["articles"] if article["collection"] in selected_groups]
    sampled_articles = filtered_articles[:5]
    # images_list = [article['url'] for article in sampled_articles]

    images_list = []
    for group in selected_groups:
        group_name_dashed = group.replace(' ', '_').strip()
        img_url = cluster[f'{group_name_dashed}_summary']['image_url']
        images_list.append(img_url)

    images = [fetch_image(url) for url in images_list]

    return images


def calculate_total_and_percentage(cluster, selected_groups, selected_week):
    # total_articles = sum(c['article_counts'] for c in data[selected_week])
    total_articles = cluster['mostly_left_summary']['total_num_articles']
    selected_articles_count = sum(v for k, v in cluster["distribution"].items() if k in selected_groups)
    percentage = (selected_articles_count / total_articles) * 100
    return selected_articles_count, percentage

@st.cache_data
def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='gray', prefer_horizontal=1.0).generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig




def download_cluster_data_as_csv(cluster, week, selected_groups, is_duplicate=False):
    articles_data = []
    for article in cluster["articles"]:
        if article["collection"] in selected_groups:
            articles_data.append({
                "Title": article["title"],
                "collection": article["collection"],
                "URL": article["url"]
            })
    df = pd.DataFrame(articles_data)
    csv = df.to_csv(index=False)

    if is_duplicate:
        file_name = f"{cluster['name']}_week_{week}_1.csv"
    else:
        file_name = f"{cluster['name']}_week_{week}.csv"

    st.download_button(
        label="Download Data as CSV",
        data=csv,
        file_name=file_name,
        mime="text/csv"
    )


def add_placeholder(): # This adds an empty block. I use this to align both columns.
    placeholder_button_style = """
                <style>
                .placeholder-button {
                    background-color: #FFFFFF;
                    color: white;
                    border: none;
                    padding: 20px 20px;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    text-align: center;
                    display: inline-block;
                }
                .placeholder-button:hover {
                    background-color: #FFFFFF;
                }
                .placeholder-button:focus {
                    outline: none;
                }
                </style>
                """
    st.markdown(placeholder_button_style, unsafe_allow_html=True)
    placeholder_button_html = f"""
                <div style='text-align: center;'>
                    <button class="placeholder-button"></button>
                </div>
                """
    st.markdown(placeholder_button_html, unsafe_allow_html=True)


def create_cluster_page():
    params = st.experimental_get_query_params()
    selected_week = params.get("week", ["2024-07-08 to 2024-07-14"])[0]
    cluster_index = int(params.get("cluster", [0])[0])

    if selected_week not in data:
        st.markdown('Select a valid week!')
        return

    if params.get("collection"):
        initial_selected_group = params.get("collection")[0]
    else:
        initial_selected_group = None


    # main_cluster = data[selected_week][cluster_index]

    # st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    # download_cluster_data_as_csv(main_cluster, selected_week)
    # st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "<h1>Compare Media Coverage</h1>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h2>First Set</h2>",
            unsafe_allow_html=True
        )


        cluster_names = [c["name"] for c in data[selected_week]]
        selected_cluster_name = st.selectbox("Change first set:", cluster_names, index=cluster_index)
        main_cluster = get_cluster_data(selected_cluster_name, selected_week)

        group_options = list(main_cluster["distribution"].keys())
        initial_options = group_options

        if initial_selected_group:
            initial_options = [initial_selected_group]

        selected_groups = st.multiselect("Select collections in the first cluster:", group_options, default=initial_options)

        if len(selected_groups) < len(group_options):
            selected_groups.append("Other")

        if "Other" in selected_groups:
            selected_groups.remove("Other")

        add_placeholder()



        st.markdown("---")

        download_cluster_data_as_csv(main_cluster, selected_week, selected_groups)

        total_articles, percentage = calculate_total_and_percentage(main_cluster, selected_groups, selected_week)
        st.markdown(f"**Percentage:** {percentage:.2f}%")
        st.markdown(f"**Number of Articles:** {total_articles}")

        pie_chart_placeholder = st.empty()
        pie_chart = create_pie_chart(main_cluster, selected_groups)
        pie_chart_placeholder.plotly_chart(pie_chart, use_container_width=True)

        sample_images = display_sample_images(main_cluster, selected_groups)
        st.markdown("### Top Images")
        image_columns = st.columns(5)
        for col, img in zip(image_columns, sample_images):
            col.image(img, use_column_width=True)

        st.markdown("### Top Terms from Headlines")
        cluster_text = " ".join(
            [remove_stopwords(article["title"]) for article in main_cluster["articles"] if article['collection'] in selected_groups])
        wordcloud_placeholder = st.empty()
        wordcloud_placeholder.pyplot(generate_word_cloud(cluster_text))

        sample_articles = display_sample_articles(main_cluster, selected_groups)
        st.markdown("### Sample Articles")
        st.markdown("\n".join(sample_articles))

    with col2:
        st.markdown(
            "<h2>Second Set</h2>",
            unsafe_allow_html=True
        )

        other_cluster_names = [c["name"] for c in data[selected_week]]  # if c["name"] != main_cluster["name"]

        selected_other_cluster_name = st.selectbox("Select second set:", other_cluster_names)
        other_cluster = get_cluster_data(selected_other_cluster_name, selected_week)

        other_group_options = list(other_cluster["distribution"].keys())
        initial_other_options = other_group_options

        if initial_selected_group:
            initial_other_options = [initial_selected_group]

        selected_other_groups = st.multiselect("Select collections in the second cluster:", other_group_options,
                                               default=initial_other_options)
        if len(selected_other_groups) < len(other_group_options):
            selected_other_groups.append("Other")

        total_articles, percentage = calculate_total_and_percentage(other_cluster, selected_other_groups, selected_week)

        show_comparison = st.button("Compare")

        if show_comparison:
            if "Other" in selected_other_groups:
                selected_other_groups.remove("Other")



            st.markdown("---")

            if other_cluster == main_cluster:
                download_cluster_data_as_csv(other_cluster, selected_week, selected_other_groups, is_duplicate=True)
            else:
                download_cluster_data_as_csv(other_cluster, selected_week, selected_other_groups)

            st.markdown(f"**Percentage:** {percentage:.2f}%")
            st.markdown(f"**Number of Articles:** {total_articles}")

            other_pie_chart_placeholder = st.empty()
            other_pie_chart = create_pie_chart(other_cluster, selected_other_groups)
            other_pie_chart_placeholder.plotly_chart(other_pie_chart, use_container_width=True)

            other_sample_images = display_sample_images(other_cluster, selected_other_groups)
            st.markdown("### Top Images")
            image_columns = st.columns(5)
            for col, img in zip(image_columns, other_sample_images):
                col.image(img, use_column_width=True)

            st.markdown("### Top Terms from Headlines")
            cluster_text = " ".join(
                [remove_stopwords(article["title"]) for article in other_cluster["articles"] if article['collection'] in selected_other_groups])
            wordcloud_placeholder = st.empty()
            wordcloud_placeholder.pyplot(generate_word_cloud(cluster_text))

            other_sample_articles = display_sample_articles(other_cluster, selected_other_groups)
            st.markdown("### Sample Articles")
            st.markdown("\n".join(other_sample_articles))

create_cluster_page()
