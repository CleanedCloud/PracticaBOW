import numpy as np


class Kmeans:
    def __init__(self) -> None:
        super().__init__()

    def create_clusters(self, data, k, num_iterations=100):
        centroids = data[np.random.choice(data.shape[0], k, replace=False)]
        for _ in range(num_iterations):
            distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
            labels = np.argmin(distances, axis=1)
            new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
            if np.all(centroids == new_centroids):
                break
            centroids = new_centroids
        return labels
