# K-Means Customer Segmentation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Load dataset
data = pd.read_csv("Mall_Customers.csv")

print("First 5 rows of the dataset:")
print(data.head())

# 2. Select features for clustering
X = data[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# 3. Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Find optimal clusters using Elbow Method
distortions = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    distortions.append(kmeans.inertia_)

plt.plot(K, distortions, "bx-")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal k")
plt.show()

# 5. Apply KMeans with chosen k (let’s pick 5 based on elbow)
kmeans = KMeans(n_clusters=5, random_state=42)
data["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nCluster counts:")
print(data["Cluster"].value_counts())

# 6. Visualize clusters in 3D
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(
    data["Age"], data["Annual Income (k$)"], data["Spending Score (1-100)"],
    c=data["Cluster"], cmap="rainbow"
)
ax.set_xlabel("Age")
ax.set_ylabel("Annual Income (k$)")
ax.set_zlabel("Spending Score")
ax.set_title("Customer Segments")
plt.show()

# 7. Show cluster centers
centers = scaler.inverse_transform(kmeans.cluster_centers_)
centers_df = pd.DataFrame(centers, columns=["Age", "Annual Income (k$)", "Spending Score (1-100)"])
print("\nCluster Centers (approximate profiles):")
print(centers_df)
