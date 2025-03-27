import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets

# Load the iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Remove the species column (not needed for clustering)
newiris = df.copy()

# Perform K-Means clustering with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(newiris)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Plot the clustering results
plt.figure(figsize=(8, 6))
plt.scatter(newiris.iloc[:, 0], newiris.iloc[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("K-Means Clustering of Iris Data")
plt.legend()
plt.grid()

# Save the plot as PNG
plt.savefig("kmeans_clusters.png")
plt.show()
