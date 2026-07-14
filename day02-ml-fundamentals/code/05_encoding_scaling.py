"""
Day 2 - Step 5: Encoding Categoricals + Feature Scaling
"""
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler, RobustScaler
import pandas as pd

# Prepare df copy for ML
df_ml = df.copy()

# 1. Label Encode 'sex'
le = LabelEncoder()
df_ml['sex_encoded'] = le.fit_transform(df_ml['sex'])  # male=1, female=0

# 2. One-Hot Encode 'embarked'
df_ml = pd.get_dummies(df_ml, columns=['embarked'], drop_first=True)

# 3. Ordinal mapping of class
class_map = {'First': 3, 'Second': 2, 'Third': 1}
df_ml['class_encoded'] = df_ml['class'].map(class_map)

# Select ML Features and Target
ml_features = ['pclass', 'sex_encoded', 'age', 'fare', 'family_size', 'is_alone',
               'embarked_Q', 'embarked_S']
X = df_ml[ml_features]
y = df_ml['survived']

print("Encoded Features DataFrame (X):")
X.head()

# --- Scaling comparison ---
std_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()
robust_scaler = RobustScaler()

scaled_std = std_scaler.fit_transform(X[['age', 'fare']])
scaled_minmax = minmax_scaler.fit_transform(X[['age', 'fare']])
scaled_robust = robust_scaler.fit_transform(X[['age', 'fare']])

print("Original scale (first 3 rows):")
print(X[['age', 'fare']].head(3).values)
print("\nStandardScaler output (first 3 rows):")
print(scaled_std[:3])
print("\nMinMaxScaler output (first 3 rows):")
print(scaled_minmax[:3])
print("\nRobustScaler output (first 3 rows):")
print(scaled_robust[:3])