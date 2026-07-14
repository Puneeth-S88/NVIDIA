"""
Day 2 - Step 6: Feature Selection + PCA
"""
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest, f_classif, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. SelectKBest (Select top 4 features based on F-value)
k_best = SelectKBest(score_func=f_classif, k=4)
k_best.fit(X, y)
k_best_indices = k_best.get_support(indices=True)
selected_k_best = [ml_features[i] for i in k_best_indices]
print(f"SelectKBest (K=4) Selected Features: {selected_k_best}")

# 2. RFE (Select top 4 features using Logistic Regression)
estimator = LogisticRegression(max_iter=500, random_state=42)
rfe = RFE(estimator=estimator, n_features_to_select=4)
rfe.fit(X, y)
rfe_indices = [i for i, val in enumerate(rfe.support_) if val]
selected_rfe = [ml_features[i] for i in rfe_indices]
print(f"RFE (N=4) Selected Features: {selected_rfe}")

# --- PCA ---
X_standardized = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_standardized)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette='Set1', alpha=0.8)
plt.title('PCA Projection of Titanic Passengers')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

print(f"Explained Variance Ratio by Component: {pca.explained_variance_ratio_}")
print(f"Total Explained Variance: {pca.explained_variance_ratio_.sum():.2%}")