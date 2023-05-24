import networkx as nx
import numpy as np
from .text_pre_process import create_sentences_embedding
from .clustering_embedding import clustering_embedding

def summarize_text(text, percentage):
    summary = ''

    sentences_embedding, n_sentences, sentences = create_sentences_embedding(text)
    n_clusters = round(n_sentences*percentage/100)
    if (n_clusters<1):
        nclusters = 1
    clusters, similarity_matrix = clustering_embedding(sentences_embedding, n_clusters)

    for i in range(n_clusters):
        cluster_indices = np.where(clusters.labels_ == i)[0]
        cluster_similarity = similarity_matrix[cluster_indices][:, cluster_indices]

        graph = nx.from_numpy_array(cluster_similarity)

        scores = nx.pagerank(graph)

        centroid_score = 0
        centroid_index = -1
        for j in range(len(cluster_indices)):
            if scores[j] > centroid_score:
                similarity_to_others = [cluster_similarity[j][k] for k in range(len(cluster_indices)) if k != j]
                if all(similarity >= 0.8 for similarity in similarity_to_others):
                    centroid_score = scores[j]
                    centroid_index = j

        if centroid_index != -1:
            summary += sentences[cluster_indices[centroid_index]].capitalize() + ' '
    return summary
