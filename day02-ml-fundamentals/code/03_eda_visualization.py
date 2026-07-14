"""
Day 2 - Step 3: Exploratory Data Analysis & Visualization
Run after 02_data_cleaning.py in the same session (so `df` exists).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# --- Outlier visualization ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.boxplot(ax=axes[0], x=df["fare"], color="lightblue")
axes[0].set_title("Boxplot of Fare")
sns.boxplot(ax=axes[1], x=df["age"], color="lightsalmon")
axes[1].set_title("Boxplot of Age")
plt.show()

# 1. IQR Method for Fare
Q1 = df["fare"].quantile(0.25)
Q3 = df["fare"].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
outliers_iqr = df[(df["fare"] < lower_limit) | (df["fare"] > upper_limit)]
print(
    f"IQR Method: Detected {len(outliers_iqr)} outliers in 'fare' "
    f"(limits: {lower_limit:.2f} to {upper_limit:.2f})"
)

# 2. Z-Score Method for Fare
z_scores = np.abs(stats.zscore(df["fare"]))
outliers_z = df[z_scores > 3]
print(f"Z-Score Method (threshold=3): Detected {len(outliers_z)} outliers in 'fare'")

# --- Survival patterns ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.countplot(ax=axes[0], data=df, x="pclass", hue="survived", palette="viridis")
axes[0].set_title("Survival by Passenger Class")
sns.barplot(ax=axes[1], data=df, x="sex", y="survived", palette="muted", ci=None)
axes[1].set_title("Survival Rate by Gender")
plt.show()

# Age distribution by survival status
plt.figure(figsize=(10, 5))
sns.kdeplot(data=df, x="age", hue="survived", fill=True, palette="crest", alpha=0.5)
plt.title("Passenger Age Distribution by Survival")
plt.xlabel("Age")
plt.show()

# --- Correlation heatmap ---
numerical_cols = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numerical_cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, vmin=-1, vmax=1
)
plt.title("Correlation Matrix of Numerical Features")
plt.show()