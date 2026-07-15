"""
Day 3 - Part 1: Environment Setup & Data Exploration
Dataset: Wisconsin Breast Cancer (built into sklearn)
Goal: predict malignant vs benign tumor -> CLASSIFICATION problem
"""
import random
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

print("Environment ready.")

# 1. Load and inspect the dataset
data = load_breast_cancer(as_frame=True)
X = data.data.copy()
y = data.target.copy()

df = X.copy()
df["target"] = y
df["target_name"] = df["target"].map({0: "malignant", 1: "benign"})

print("Feature matrix shape:", X.shape)
print("Target distribution:")
print(df["target_name"].value_counts().to_frame("count"))
print(df.head())

# Basic data-quality checks
summary = pd.DataFrame({
    "dtype": X.dtypes.astype(str),
    "missing_values": X.isna().sum(),
    "unique_values": X.nunique()
})
print(summary.head(10))

print("Total missing values:", int(X.isna().sum().sum()))
print("Duplicate rows:", int(X.duplicated().sum()))

# 2. Visualize class distribution and selected features
class_counts = df["target_name"].value_counts()
class_counts.plot(kind="bar", title="Class Distribution")
plt.xlabel("Class")
plt.ylabel("Number of samples")
plt.xticks(rotation=0)
plt.show()

selected_features = ["mean radius", "mean texture", "mean perimeter", "mean area"]
df[selected_features].hist(figsize=(10, 7), bins=20)
plt.suptitle("Selected Feature Distributions")
plt.tight_layout()
plt.show()