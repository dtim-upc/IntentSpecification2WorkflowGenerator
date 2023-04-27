import pandas as pd
from sklearn.cluster import KMeans


def sklearn_kmeans(dataset, **params):
    kmeans = KMeans(n_clusters=params['n_clusters'])
    clustered_dataset = dataset.copy().dropna()
    clustering_columns = clustered_dataset[clustered_dataset.select_dtypes(include=['number']).columns]
    labels = kmeans.fit_predict(clustering_columns)
    clustered_dataset['label'] = labels
    centroid_dataset = pd.DataFrame(kmeans.cluster_centers_, columns=clustering_columns.columns)
    return clustered_dataset, centroid_dataset
