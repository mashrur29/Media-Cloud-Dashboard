import streamlit as st
import random
from helpers import get_data
import sys

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

args = sys.argv[1:]
clusters = get_data(args[0])

sidebar_logo = 'assets/mediacloud-logo-black-2x.png'
main_body_logo = 'assets/mediacloud-logo-black-2x.png'
st.logo(sidebar_logo, icon_image=main_body_logo)

def sample_articles(articles, n=20):
    return random.sample(articles, min(n, len(articles)))



def get_articles_by_group(week_clusters, group):
    articles = []
    for cluster in week_clusters:
        articles.extend([article for article in cluster['articles'] if article['collection'] == group])
    return articles

def create_dev_view():
    params = st.experimental_get_query_params()


    st.title("Weekly Article Clusters and Collections")

    st.header("Select a data file")
    week_names = list(clusters.keys())
    selected_week = st.selectbox("Choose a file:", week_names)

    if selected_week:
        week_clusters = clusters[selected_week]

        st.header("Select a Cluster")
        cluster_names = [cluster["name"] for cluster in week_clusters]
        selected_cluster = st.selectbox("Choose a cluster:", cluster_names)

        if selected_cluster:
            if st.button(f"Refresh Cluster Sample"):
                st.experimental_set_query_params()

            st.subheader(f"Articles in cluster: {selected_cluster}")
            cluster = next((c for c in week_clusters if c["name"] == selected_cluster), None)

            if cluster:
                sample_size = 20
                articles_sample = sample_articles(cluster["articles"], sample_size)
                for article in articles_sample:
                    st.write(f"- [{article['title']}]({article['url']})")

        st.header("Select a Collection")
        groups = ["mostly left", "somewhat left", "center", "somewhat right", "mostly right"]
        selected_group = st.selectbox("Choose a collection:", groups)

        if selected_group:
            if st.button(f"Refresh Collection Sample"):
                st.experimental_set_query_params()

            st.subheader(f"Articles in collection: {selected_group}")
            group_articles = get_articles_by_group(week_clusters, selected_group)

            if group_articles:
                articles_sample = sample_articles(group_articles, 20)
                for article in articles_sample:
                    st.write(f"- [{article['title']}]({article['url']})")


create_dev_view()