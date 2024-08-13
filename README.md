# Media-Cloud-Dashboard

This is the code for Mediacloud's dashboard for analyzing media data related to the US election. This dashboard enables users to analyze and visualize clusters of news articles based on various partisan media collections such as "far left," "center left," "center," "center right," and "right." The dashboard enables users to interact with clusters, compare clusters, and view the history of news clusters across multiple collections.

## Python Files

### `home.py`

- This is the main application file that provides an overview of clusters and collections for the selected weeks.
- **Workflow**:
  - Allows the user to select a week from a dropdown menu.
  - Displays a treemap visualization of the news clusters for the week.
  - Displays the treemap visualizations of the news clusters for all collection.

### `cluster_page.py`

- Provides the details of a cluster and allows comparison between clusters
- **Workflow**:
  - Extracts query parameters from `home.py` to determine the selected week and cluster.
  - Displays information about the selected cluster, including a pie chart of the distribution of articles across different groups, top images, a wordcloud of frequent words, and sample article titles.
  - Allows the user to compare the selected cluster with another cluster, showing similar details for the compared cluster.

### `collection_page.py`

- Provides the details of a collection
- **Workflow**:
  - Extracts query parameters from `home.py` to determine the selected week and collection.
  - Displays information about the selected cluster, including a pie chart of the distribution of articles in that particular collection, and treemap visualizations of the cluster for that group across several weeks.

## Installation and Running the Dashboard

### Prerequisites

- Python 3.10.14
- pip (Python package installer)

### Installation

1. **Create and activate a virtual environment**:
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install spacy packages** (lines 6-7 in helpers.py): 
    ```bash
    nltk.download('stopwords')
    ```
   ```bash
    nltk.download('punkt_tab')
    ```

### Running the Program

1. **Start the Streamlit server for the main application**:
    ```bash
    streamlit run home.py data/
    ```