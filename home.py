import streamlit as st
import plotly.graph_objects as go
import random
import textwrap
import plotly.express as px
import pandas as pd
import urllib.parse
import sys

from helpers import get_data, group_colors

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

args = sys.argv[1:]
data = get_data(args[0])

base_url = 'http://localhost:8501'

sidebar_logo = 'assets/mediacloud-logo-black-2x.png'
main_body_logo = 'assets/mediacloud-logo-black-2x.png'
st.logo(sidebar_logo, icon_image=main_body_logo)

def add_floating_button_pageup():
    floating_button_html = """
    <style>
    .scroll-to-top {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #D84424;
        color: white;
        border: none;
        padding: 10px 15px;
        border-radius: 50%;
        font-size: 18px;
        cursor: pointer;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
    <a target="_self" href="#media-cloud-election-dashboard">
    <button onclick="window.scrollTo({top: 0, behavior: 'smooth'});" class="scroll-to-top">&#8679;</button>
    </a>
    """
    st.markdown(floating_button_html, unsafe_allow_html=True)


def display_group_legend():
    legend_html = """
    <div style='display: flex; justify-content: left; align-items: center; margin-top: 20px;'>
        <div style='margin-right: 20px;'><b>Each Cluster Encompasses Articles from Five Media Collections:</b></div>
        <div style='display: flex; flex-wrap: wrap; justify-content: center;'>
    """
    for group, color in group_colors.items():
        url_group_name = 'clusters-for-' + group.replace(' ', '-')
        encoded_group_name = urllib.parse.quote(url_group_name)
        # legend_html += f"<div style='background-color: {color}; color: white; padding: 5px 10px; margin: 5px; border-radius: 5px;'>{group.replace('%20', ' ').capitalize()}</div>"
        legend_html += f"<a href='#{encoded_group_name}' style='background-color: {color}; color: white; padding: 5px 10px; margin: 5px; border-radius: 5px; text-decoration: none;'>{group.replace('%20', ' ').capitalize()}</a>"
    legend_html += "</div></div>"
    st.markdown(legend_html, unsafe_allow_html=True)


def display_individual_group_title(group, url_group):
    legend_html = """
        <div style='display: flex; justify-content: left; align-items: center; margin-top: 20px;'>
            <div style='margin-right: 20px;'><b>Clusters for</b></div>
            <div style='display: flex; flex-wrap: wrap; justify-content: center;'>
        """

    color = group_colors[group]
    legend_html += f"<a href='{url_group}' style='background-color: {color}; color: white; padding: 5px 10px; margin: 5px; border-radius: 5px; text-decoration: none;'>{group.replace('%20', ' ').capitalize()}</a>"
    legend_html += "</div></div>"
    st.markdown(legend_html, unsafe_allow_html=True)

def display_sample_articles(cluster_name, clusters, group=None):
    cluster = next(c for c in clusters if c["name"] == cluster_name)
    articles = cluster["articles"]
    if group:
        articles = [article for article in articles if article["collection"] == group]
    sampled_articles = random.sample(articles, min(5, len(articles)))
    articles_list = [f"- {article['title']}" for article in sampled_articles]
    return "<br>".join(articles_list)


def wrap_text(text, max_words=3):
    words = text.split()
    wrapped_text = '<br>'.join([' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)])
    return wrapped_text



def create_main_treemap(labels, values, colors, urls):
    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=[""] * len(labels),
        values=values,
        marker=dict(colors=colors, showscale=False, line=dict(color='black', width=0.5)),
        texttemplate="<b><a href='%{customdata}' style='text-decoration: underline;'>%{label}</a></b>",
        textposition="middle center",
        textinfo="label+value+text",
        hoverinfo="label+value+text",
        customdata=urls,
        text=labels,
        textfont=dict(size=18)
    ))

    return fig


if 'selected_label' not in st.session_state:
    st.session_state.selected_label = None


def treemap_callback(trace, points, selector):
    st.session_state.selected_label = points.label



def create_cluster_group_treemap_hierarchical(clusters): # No longer used
    labels = []
    parents = []
    values = []
    texts = []
    colors = []

    for cluster in clusters:
        cluster_name = cluster['name']
        cluster_articles = cluster['article_counts']
        labels.append(cluster_name)
        parents.append("")
        values.append(cluster_articles)
        texts.append(f"Total Articles: {cluster_articles}")
        colors.append(cluster['color'])

        for group, count in cluster['distribution'].items():
            labels.append(f"{group.title()}")
            parents.append(cluster_name)
            values.append(count)
            colors.append(group_colors[group])
            sample_articles = display_sample_articles(cluster_name, clusters, group)
            texts.append(f"Sample articles: <br> {sample_articles}")

    fig = go.Figure(go.Treemap(
        labels=labels,
        parents=parents,
        values=values,
        textinfo="label+value+text",
        hoverinfo="label+value+text",
        text=texts,
        texttemplate="<b>%{label}</b><br>%{text}",
        textposition="middle center",
        marker=dict(colors=colors, showscale=False),
        tiling=dict(packing="binary"),
        textfont=dict(size=20)
    ))

    fig.update_traces(
        hovertemplate='<b>%{label}</b><br>Number of Articles: %{value}<br>%{text}',
        selector=dict(type='treemap'),
        pathbar=dict(visible=True)
    )

    fig.update_layout(height=700)
    fig.update_traces(marker=dict(cornerradius=10))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    return fig





def create_group_treemap(group_name, clusters, total_articles, selected_week, colors):
    group_articles = []
    group_values = []
    group_color_values = []
    group_labels = []
    group_full_labels = []
    group_urls = []
    group_sample_texts = []

    for i, cluster in enumerate(clusters):
        group_count = sum(1 for article in cluster['articles'] if article['collection'] == group_name)

        if group_count > 0:
            group_name_dashed = group_name.replace(' ', '_').strip()
            cluster_group_headline = cluster[f'{group_name_dashed}_summary']['article']['title']


            group_articles.append(group_count)
            group_values.append(group_count)
            group_color_values.append(((group_count / total_articles) * 100))
            group_labels.append(wrap_text(cluster_group_headline))
            group_full_labels.append(cluster_group_headline)
            group_urls.append(f"/cluster_page?week={selected_week}&cluster={i}&collection={group_name}")
            group_sample_texts.append(display_sample_articles(cluster['name'], clusters))

    if group_values:
        fig = go.Figure(go.Treemap(
            labels=group_labels,
            parents=[""] * len(group_labels),
            values=group_values,
            textinfo="label+value+text",
            hoverinfo="label+value+text",
            text=group_sample_texts,
            texttemplate="<b><a href='%{customdata}' style='text-decoration: underline;'>%{label}</a></b>",
            customdata=group_urls,
            textposition="middle center",
            marker=dict(colors=colors, showscale=False, line=dict(color='black', width=0.5)),
            textfont=dict(size=18)
        ))

        fig.update_traces(
            hovertemplate='<b>%{label}</b><br>Number of Articles: %{value}',
            selector=dict(type='treemap'),
            pathbar=dict(visible=True)
        )

        fig.update_layout(height=500)
        fig.update_traces(marker=dict(cornerradius=10))
        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

        return fig





def create_home_page():
    st.title("Media Cloud Election Dashboard")
    st.markdown("### Select a week to view the top clusters for that week:")

    selected_week = st.selectbox("Select a week:", list(data.keys()))
    clusters = data[selected_week]

    total_articles = sum(cluster['article_counts'] for cluster in clusters)
    values = [cluster['article_counts'] for cluster in clusters]
    color_values = [((cluster['article_counts'] / total_articles) * 100) for cluster in clusters]
    labels = [wrap_text(cluster['name']) for cluster in clusters]
    actual_labels = [cluster['name'] for cluster in clusters]
    full_labels = [cluster['name'] for cluster in clusters]
    urls = [f"/cluster_page?week={selected_week}&cluster={i}" for i in range(len(clusters))]
    sample_texts = [display_sample_articles(cluster['name'], clusters) for cluster in clusters]
    colors = [cluster['color'] for cluster in clusters]

    fig = create_main_treemap(labels, values, colors, urls)

    fig.update_traces(
        hovertemplate='<b>%{label}</b><br>Number of Articles: %{value}',
        selector=dict(type='treemap'),
        pathbar=dict(visible=True)
    )
    fig.update_layout(height=700)
    fig.update_traces(marker=dict(cornerradius=10))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))


    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")


    st.title(f"Top Clusters for {selected_week.title()} Among Different Collections")
    display_group_legend()
    st.markdown("###")


    groups = list(group_colors.keys())


    col1, col2 = st.columns(2)

    for id, group in enumerate(groups):
        group_id = group.replace(' ', "%20")
        week_id = selected_week.replace(' ', "%20")

        url_group = f'/collection_page?week={week_id}&collection={group_id}'

        if id % 2 == 0:
            with col1:
                st.markdown(
                    f"<h4>Clusters for <a href={url_group} style='color: {group_colors[group]};'>{group.capitalize()}</a></h4>",
                    unsafe_allow_html=True
                )

                group_treemap = create_group_treemap(group, clusters, total_articles, selected_week, colors)
                if group_treemap:
                    st.plotly_chart(group_treemap, use_container_width=True)
        else:
            with col2:
                st.markdown(
                    f"<h4>Clusters for <a href={url_group} style='color: {group_colors[group]};'>{group.capitalize()}</a></h4>",
                    unsafe_allow_html=True
                )

                group_treemap = create_group_treemap(group, clusters, total_articles, selected_week, colors)
                if group_treemap:
                    st.plotly_chart(group_treemap, use_container_width=True)

create_home_page()

add_floating_button_pageup()


# This code piece might be useful later ***
#
#
# def print_sample_articles(articles):
#     for article in articles:
#         st.markdown(f"- [{article['title']}]({article['url']})")
#
# st.markdown(f"#### Sample Articles of Top Topics for {selected_week.title()}")
#
# display_group_legend()
# st.markdown('#####')
#
#
# cluster_names = [cluster["name"] for cluster in data[selected_week]]
# selected_cluster_name = st.selectbox("Select a Topic:", cluster_names)
#
# selected_cluster_sample_article = next(cluster for cluster in clusters if cluster["name"] == selected_cluster_name)
#
#
# with st.expander(f'Click to View Sample Articles'):
#     st.markdown(f"**Total Articles:** {selected_cluster_sample_article['article_counts']}")
#     for group in selected_cluster_sample_article["distribution"].keys():
#         st.subheader(f"{group.title()} ({selected_cluster_sample_article['distribution'][group]} articles)")
#         sample_articles = [article for article in selected_cluster_sample_article["articles"] if article["group"] == group]
#         print_sample_articles(sample_articles[:5])
#
#
# st.markdown('#####')