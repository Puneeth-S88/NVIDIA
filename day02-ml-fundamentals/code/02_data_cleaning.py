"""
Day 2 - Step 2: Data Loading (robust) + Inspection + Cleaning
Loads the Titanic dataset with a Seaborn->GitHub fallback, inspects
its structure, then cleans missing values and duplicates.
"""
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

warnings.filterwarnings("ignore")

# Set plotting options
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
print("All standard libraries imported and plotting style initialized!")

# 1. Loading the Titanic Dataset
try:
    df = sns.load_dataset("titanic")
    print("Loaded dataset successfully from Seaborn!")
except Exception:
    print("Seaborn loading failed. Downloading from GitHub...")
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
    df = pd.read_csv(url)

print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 rows:")
df.head()

# 2. Understanding Data Types
print("=== Metadata & Data Types ===")
df.info()

print("\n=== Numerical Features Summary ===")
print(df.describe())

print("\n=== Categorical Features Summary ===")
print(df.describe(include=["object", "category"]))

# 3. Check for missing values
print("Missing values per column:")
print(df.isnull().sum())

# Impute missing Age with median
df["age"].fillna(df["age"].median(), inplace=True)

# Impute missing Embarked and Embark Town with mode
df["embarked"].fillna(df["embarked"].mode()[0], inplace=True)
df["embark_town"].fillna(df["embark_town"].mode()[0], inplace=True)

# Impute Deck: handle missing values by mapping to string and filling
df["deck"] = df["deck"].astype(str).replace("nan", "Unknown")

# Identify and remove duplicate records
duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate records found: {duplicates}")
if duplicates > 0:
    df.drop_duplicates(inplace=True)
    print("Duplicates removed successfully!")

print("\nRemaining missing values:")
print(df.isnull().sum())