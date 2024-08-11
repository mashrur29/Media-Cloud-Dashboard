import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import random
from helpers import get_data, group_colors

data = get_data()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")



def get_cluster_data(cluster_name, selected_week):
    for cluster in data[selected_week]:
        if cluster['name'] == cluster_name:
            return cluster
    return None


def wrap_text(text, max_words=3):
    words = text.split()
    wrapped_text = '<br>'.join([' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)])
    return wrapped_text

def print_sample_articles(group_name, clusters, num_samples=5):
    random.seed(random.randint(1, 100))
    articles_list = []

    for cluster in clusters:
        num_articles = len(cluster['articles'])
        count_articles = 0
        for i in range(num_articles):
            if cluster['articles'][i]['collection'] == group_name:
                articles_list.append(cluster['articles'][i])
                count_articles = count_articles + 1
            if count_articles >= 5:
                break

    sampled_articles = random.sample(articles_list, min(num_samples, len(articles_list)))

    for article in sampled_articles:
        st.markdown(f"- [{article['title']}]({article['url']})")


def create_group_treemap(selected_week, group_name, clusters, is_duplicate=False):
    labels = []
    parents = []
    values = []
    colors = [cluster['color'] for cluster in clusters]
    group_urls = []

    for i, cluster in enumerate(clusters):
        for group, count in cluster['distribution'].items():
            if group == group_name:
                labels.append(wrap_text(cluster["name"]))
                parents.append("")
                values.append(count)
                group_urls.append(f"/cluster_page?week={selected_week}&cluster={i}&collection={group_name}")

    if is_duplicate:
        fig = go.Figure(go.Treemap(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(colors=colors, showscale=False, line=dict(color='black', width=0.5)),
            hovertemplate='%{label}<br>Articles: %{value}<br>',
            texttemplate="<b><a href='%{customdata}' style='text-decoration: underline;'>%{label}</a></b>",
            customdata=group_urls,
            textposition='middle center',
            textfont=dict(size=18)
        ))
    else:
        fig = go.Figure(go.Treemap(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(colors=colors, showscale=False, line=dict(color='black', width=0.5)),
            hovertemplate='<b>%{label}</b><br>Articles: %{value}<br>',
            texttemplate="<b><a href='%{customdata}' style='text-decoration: underline;'>%{label}</a></b>",
            customdata=group_urls,
            textposition='middle center',
            textfont=dict(size=18)
        ))

    fig.update_layout(height=400)
    fig.update_traces(marker=dict(cornerradius=10))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    return fig


def create_group_pie_chart(group_name, clusters):
    total_articles = sum(cluster['article_counts'] for cluster in clusters)
    group_articles = sum(
        count for cluster in clusters for group, count in cluster['distribution'].items() if group == group_name)
    other_articles = total_articles - group_articles

    colors = [group_colors[group_name], "#5C6068"]

    fig = go.Figure(go.Pie(
        labels=[f'This group ({group_articles})', f'Other ({other_articles})'],
        values=[group_articles, other_articles],
        textinfo='label+percent',
        insidetextorientation='horizontal',
        marker=dict(colors=colors)
    ))

    fig.update_layout(showlegend=False)
    return fig


def update_treemap_piechart_curr_week(selected_week, group_name):
    clusters = data[selected_week]
    st.markdown(f"### Overall attention during {selected_week}")
    pie_chart = create_group_pie_chart(group_name, clusters)
    st.plotly_chart(pie_chart, use_container_width=True)

    st.markdown(f"### Treemap for this week")
    group_treemap = create_group_treemap(selected_week, group_name, clusters)
    st.plotly_chart(group_treemap, use_container_width=True)


def create_collection_page():
    query_params = st.experimental_get_query_params()
    group_name = query_params.get("collection", ["mostly left"])[0]
    initial_selected_week = query_params.get("week", ["week 1"])[0]

    # st.markdown("<h1> Change Group </h1>", unsafe_allow_html=True)

    group_options = list(group_colors.keys())
    group_name = st.selectbox("Select Another Collection:", group_options, index=group_options.index(group_name))

    st.markdown(
        f"<h1>Showing Clusters for Collection <span style='color: {group_colors[group_name]};'>{group_name.title()}</span></h1>",
        unsafe_allow_html=True
    )

    week_options = list(data.keys())
    selected_week = st.selectbox("Select a week:", week_options, index=week_options.index(initial_selected_week))

    clusters = data[selected_week]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"#### Overall attention for {selected_week}")
        pie_chart = create_group_pie_chart(group_name, clusters)
        st.plotly_chart(pie_chart, use_container_width=True)


    with col2:
        st.markdown(f"#### Top clusters for {selected_week}")
        group_treemap = create_group_treemap(selected_week, group_name, clusters)
        st.plotly_chart(group_treemap, use_container_width=True)


    st.markdown(f"#### Sample articles for {selected_week}")
    print_sample_articles(group_name, clusters, 5)

    st.markdown(
        f"<h1>Historical Attention Over Clusters for All Weeks for <span style='color: {group_colors[group_name]};'>{group_name.title()}</span></h1>",
        unsafe_allow_html=True
    )

    for week in reversed(list(data.keys())):
        if week != selected_week:
            st.markdown(f"#### {week.replace('%20', ' ').capitalize()}")
            week_clusters = data[week]
            week_group_treemap = create_group_treemap(week, group_name, week_clusters)
            st.plotly_chart(week_group_treemap, use_container_width=True)
        else:
            st.markdown(f"#### {week.replace('%20', ' ').capitalize()} (Selected Week)")
            week_clusters = data[week]
            week_group_treemap = create_group_treemap(week, group_name, week_clusters, is_duplicate=True)
            st.plotly_chart(week_group_treemap, use_container_width=True)

create_collection_page()
