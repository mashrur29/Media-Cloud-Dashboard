from data.test_data import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# nltk.download('stopwords')
# nltk.download('punkt_tab')

def remove_stopwords(sent):
    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(sent)
    filtered_words = [w for w in word_tokens if not w.lower() in stop_words]

    return ' '.join(filtered_words)



def get_data():
    processed_clusters = {}

    for week in clusters:

        cluster_week = []
        colors_list = ["#C8CFA0", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#DBB5B5", "#D1C4E9", "#E8C5E5", "#D6DAC8",
                       "#D7CCC8", "#DCEDC8"]

        for idx, c in enumerate(clusters[week]):
            c["color"] = colors_list[idx % 10]
            c["distribution"] = {}
            c["distribution"]["far left"] = 0
            c["distribution"]["center left"] = 0
            c["distribution"]["center"] = 0
            c["distribution"]["center right"] = 0
            c["distribution"]["right"] = 0

            for article in c["articles"]:
                if article["group"] == "far left":
                    c["distribution"]["far left"] += 1
                elif article["group"] == "center left":
                    c["distribution"]["center left"] += 1
                elif article["group"] == "center":
                    c["distribution"]["center"] += 1
                elif article["group"] == "center right":
                    c["distribution"]["center right"] += 1
                else:
                    c["distribution"]["right"] += 1

            cluster_week.append(c)

        processed_clusters[week] = cluster_week

    return processed_clusters
