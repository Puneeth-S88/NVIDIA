"""
Day 2 - Step 1: Data Loading
Tested 3 ways of loading datasets: raw CSV from GitHub, Seaborn's
built-in dataset loader, and sklearn's built-in loader.
"""
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# CSV from GitHub
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
df = pd.read_csv(url)
print(df.head())

# Seaborn dataset
print(sns.load_dataset("tips").head())

# sklearn built-in dataset
iris = load_iris(as_frame=True)
print(iris.frame.head())