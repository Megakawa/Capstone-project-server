from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering

def clustering_embedding(embedding, n_clusters):
    similarity_matrix = cosine_similarity(embedding)
    hac = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average')
    hac.fit(similarity_matrix)
    return hac, similarity_matrix

