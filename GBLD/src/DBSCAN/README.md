# 📊 DBSCAN Clustering on Distance Matrix


### 📚 Description:
This Python script performs DBSCAN (Density-Based Spatial Clustering of Applications with Noise) clustering on a precomputed distance matrix. The script identifies clusters and outliers, then prints the cluster assignments for each data point and the points within each cluster.

### 🛠️ Requirements:
- 🐍 **Python Libraries**:  
  - `numpy` (for numerical computations)
  - `sklearn` (for the DBSCAN clustering algorithm)

To install the necessary libraries, you can use:
```bash
pip install numpy scikit-learn
```

### ⚙️ How It Works:
1. **Precomputed Distance Matrix**: The input is a distance matrix, where the values represent the pairwise distances between points.
2. **DBSCAN Algorithm**: The script applies DBSCAN to the distance matrix to identify clusters. Points are grouped into clusters based on density, and points that do not belong to any cluster are labeled as outliers.
3. **Cluster and Outlier Detection**: The script identifies the number of clusters and prints outliers and the assignments of points to clusters.
4. **Output**: The script displays the outliers, the number of clusters, and the points in each cluster.

### 🔧 Usage:

#### 1️⃣ Modify the Distance Matrix:
Replace the `matrix` variable with your own precomputed distance matrix (in the form of a NumPy array).

```python
matrix = np.array([ 
    [0.0, 0.78, 1.04, 0.77, 1.13, 0.75, 0.53, 0.76, 0.49, 0.67 ], 
    # Add your distance data here
])
```

#### 2️⃣ Run the Script:
Execute the script, and it will output the clustering results, including outliers and the points belonging to each cluster.

```bash
python dbscan_clustering.py
```

### 🧑‍💻 Example Output:
After running the script, you will see the following outputs in the console:

```
Outliers are at indices: []
Number of clusters: 2
Point 0 is assigned to cluster 0
Point 1 is assigned to cluster 0
Point 2 is assigned to cluster 1
Point 3 is assigned to cluster 0
Point 4 is assigned to cluster 1
Point 5 is assigned to cluster 0
Point 6 is assigned to cluster 0
Point 7 is assigned to cluster 0
Point 8 is assigned to cluster 0
Point 9 is assigned to cluster 0
Cluster 0 contains points: [0 1 3 5 6 7 8 9]
Cluster 1 contains points: [2 4]
```

- **Outliers**: The script identifies the outliers (points that don't belong to any cluster).
- **Number of Clusters**: The script prints the total number of clusters detected.
- **Cluster Assignments**: Each point’s assigned cluster is displayed.
- **Cluster Contents**: The points that belong to each cluster are listed.

### 📁 File Structure:
```bash
|-- dbscan_clustering.py   # Main script
|-- distance_matrix.npy    # Your precomputed distance matrix (if applicable)
```

### 🧑‍💻 How DBSCAN Works:
DBSCAN is a clustering algorithm that groups together closely packed points, marking as outliers points that lie alone in low-density regions. The two main parameters:
- `eps` (epsilon): The maximum distance between two points to be considered neighbors.
- `min_samples`: The minimum number of points required to form a dense region (i.e., a cluster).
