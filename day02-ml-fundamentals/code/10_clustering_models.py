"""
Day 2 - Step 10: Clustering (Passenger Segmentation using Age & Fare)
"""
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

X_clust = StandardScaler().fit_transform(df[['age', 'fare']])

# A. K-Means Elbow Method to choose optimal clusters
wcss = []
for i in range(1, 11):
    km = KMeans(n_clusters=i, init='k-means++', random_state=42)
    km.fit(X_clust)
    wcss.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('K-Means Elbow Curve')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia (WCSS)')
plt.show()

# Train K-Means (K=3)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X_clust)

# B. Hierarchical (Agglomerative) Clustering (N=3)
agg_clust = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_clust.fit_predict(X_clust)

# C. DBSCAN Clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_clust)

# Visualize passenger segments using K-Means
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['age'], y=df['fare'], hue=kmeans_labels, palette='viridis', alpha=0.8)
plt.yscale('log')
plt.title('Passenger Profiles Identified by K-Means')
plt.xlabel('Age')
plt.ylabel('Fare (Log Scale)')
plt.show()