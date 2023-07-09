import os
import json
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


load_dotenv("../.env")
key = os.getenv("azure_cv_key")
endpoint = os.getenv("azure_cv_endpoint")

st.title("Dataset Clustering")


@st.cache_data
def fetch_files(directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


def dataset_clustering():
    with open("img_embeddings.json") as f:
        list_emb = json.load(f)

    k_values = range(2, 20)
    silhouette_scores = []
    max_val = []

    for k in k_values:
        kmeans = KMeans(n_clusters=k, random_state=123456)
        kmeans.fit(list_emb)
        labels = kmeans.labels_
        score = silhouette_score(list_emb, labels)
        max_val.append(score)
        max_val.sort(reverse=True)
        silhouette_scores.append(score)

        print(
            f"For k = {k:02} => Silhouette score = {score:.5f} | Maximum score = {max_val[0]:.5f}"
        )

    OUTPUT_DIR = "output"

    # os.makedirs(OUTPUT_DIR, exist_ok=True)
    #
    # plt.figure(figsize=(10, 5))
    # plt.plot(k_values, silhouette_scores, color="blue")
    # plt.title("Silhouette scores clustering on images vector embeddings", size=10)
    # plt.grid(True, color="grey", linestyle="--")
    #
    # for k, silh in zip(k_values, silhouette_scores):
    #     plt.text(k, silh, f"{silh:.5f}")
    #
    # plt.xticks(k_values)
    # plt.xlabel("Number of clusters (k)")
    # plt.ylabel("Silhouette score")
    # plt.tight_layout()
    #
    # plt.savefig(os.path.join(OUTPUT_DIR, "silhouette_plot.png"))

    nb_clusters = 17

    kmeans = KMeans(n_clusters=nb_clusters,
                    random_state=123456)

    kmeans.fit(list_emb)
    labels = kmeans.labels_

    cluster_series = pd.Series(labels, name="cluster")
    df_clusters = pd.DataFrame(
        {"image_file": fetch_files("./fashion_dataset"), "vector": list_emb, "cluster": labels}
    )

    # Define number of images to display per cluster
    num_images_per_cluster = 5

    # Get list of clusters in DataFrame
    clusters = df_clusters["cluster"].unique()
    # Sorted list
    clusters = np.sort(clusters)

    # Create figure with subplots
    num_rows = len(clusters)
    fig, axes = plt.subplots(num_rows, num_images_per_cluster, figsize=(20, 5*num_rows))

    # Display images on subplots
    for i, cluster in enumerate(clusters):
        # Get rows in DataFrame for current cluster
        cluster_rows = df_clusters[df_clusters["cluster"] == cluster].head(num_images_per_cluster)
        for j, row in enumerate(cluster_rows.itertuples(index=False)):
            img = Image.open(row.image_file)
            axes[i, j].imshow(img)
            axes[i, j].set_title(f"Cluster {row.cluster}")
            axes[i, j].axis("off")

    plt.savefig(os.path.join(OUTPUT_DIR, "cluster.png"))

    cluster_labels = [
        "0", "Shoes",
        "1", "Shorts",
        "2", "Woman clothes",
        "3", "Sheets",
        "4", "Colored Woman shirts",
        "5", "Woman T shirts",
        "6", "Accessories",
        "7", "Coats",
        "8", "Jumpers",
        "9", "Sportwear shirts",
        "10", "Lingerie",
        "11", "Colored shirts",
        "12", "Dresses",
        "13", "Trousers",
        "14", "Shirts",
        "15", "Glasses and caps",
        "16", "Fancy clothes",
    ]

    cluster_ids = [int(cluster_labels[i]) for i in range(0, len(cluster_labels), 2)]
    category_names = [cluster_labels[i + 1] for i in range(0, len(cluster_labels), 2)]

    cluster_ids_series = pd.Series(cluster_ids, name="cluster")
    cluster_names_series = pd.Series(category_names, name="cluster_label")
    cluster_labels_df = pd.concat([cluster_ids_series, cluster_names_series], axis=1)
    df_results = pd.merge(df_clusters, cluster_labels_df, on="cluster", how="left")
    # Adding 1 to avoid the number 0
    df_results["cluster"] = df_results["cluster"].apply(lambda x: int(x) + 1)
    # Numbers in 2 characters
    df_results["cluster"] = df_results["cluster"].apply(
        lambda x: f"0{x}" if int(x) < 10 else x
    )
    # Adding some text
    df_results["cluster"] = df_results["cluster"].astype(str)
    df_results["Cluster and Label"] = (
            "Cluster " + df_results["cluster"] + " = " + df_results["cluster_label"]
    )

    df_results.to_json(os.path.join(OUTPUT_DIR, "clusters.json"))
    ax = (
        df_results["Cluster and Label"]
        .value_counts()
        .plot(
            kind="barh",
            figsize=(10, 7),
            title="Number of images per cluster",
            color="purple",
        )
    )

    ax.set_xlabel("cluster")
    ax.set_ylabel("Frequency")


    st.image("./output/cluster.png")


dataset_clustering()
