
import numpy as np
from sklearn.cluster import DBSCAN

# Your distance matrix
matrix = np.array([
    [0.0, 0.78, 1.04, 0.77, 1.13, 0.75, 0.53, 0.76, 0.49, 0.67 ],
    [0.78, 0.0, 1.13, 0.44, 1.23, 0.88, 0.7, 0.96, 0.74,  0.64 ],
    [1.04, 1.13, 0.0, 1.14, 0.49, 1.07, 0.98, 0.92, 1.01, 1.01 ],
    [0.77, 0.44, 1.14, 0.0, 1.24, 0.93, 0.69, 0.98, 0.77, 0.72],
    [1.13, 1.23, 0.49, 1.24, 0.0, 1.14, 1.11, 0.98, 1.04, 1.12],
    [0.75, 0.88, 1.07, 0.93, 1.14, 0.0, 0.71, 0.89, 0.69, 0.81],
    [0.53, 0.7, 0.98, 0.69, 1.11, 0.71, 0.0, 0.81, 0.59, 0.52],
    [0.76, 0.96, 0.92, 0.98, 0.98, 0.89, 0.81, 0.0, 0.84, 0.66],
    [0.49, 0.74, 1.01, 0.77, 1.04, 0.69, 0.59, 0.84, 0.0, 0.89 ],
    [0.67, 0.64, 1.01, 0.72, 1.12, 0.81, 0.52, 0.66, 0.89, 0.0 ]
])
# Apply DBSCAN
db = DBSCAN(eps=0.7, min_samples=2, metric='precomputed')
labels = db.fit_predict(matrix)

# Find outliers and clusters
outliers = np.where(labels == -1)[0]
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

print(f"Outliers are at indices: {outliers}")
print(f"Number of clusters: {n_clusters}")

# Print cluster assignments
for i, label in enumerate(labels):
    print(f"Point {i} is assigned to cluster {label}")

# Print points in each cluster
unique_labels = set(labels)
for label in unique_labels:
    if label != -1:
        cluster_points = np.where(labels == label)[0]
        print(f"Cluster {label} contains points: {cluster_points}")
