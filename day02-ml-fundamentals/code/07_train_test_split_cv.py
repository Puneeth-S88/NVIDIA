"""
Day 2 - Step 7: Train/Test Split, Cross-Validation, Class Imbalance
"""
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print(f"Training Set: {X_train.shape[0]} rows")
print(f"Test Set:     {X_test.shape[0]} rows")

# --- 5-Fold Cross Validation ---
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_model = LogisticRegression(max_iter=500, random_state=42)
scores = cross_val_score(cv_model, X_train, y_train, cv=kfold, scoring='accuracy')

print(f"K-Fold Scores: {scores}")
print(f"Mean CV Accuracy: {scores.mean():.4f} +/- {scores.std():.4f}")

# --- Class imbalance handling ---
print("Original Target Class Distribution:")
print(y_train.value_counts(normalize=True))

try:
    from imblearn.over_sampling import SMOTE

    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
    print("\nSMOTE applied using imblearn successfully!")

except ImportError:
    print("\nimblearn library not installed. Running manual resampling fallback...")
    df_temp = pd.concat([X_train, y_train], axis=1)
    df_maj = df_temp[df_temp['survived'] == 0]
    df_min = df_temp[df_temp['survived'] == 1]

    df_min_oversampled = df_min.sample(len(df_maj), replace=True, random_state=42)
    df_oversampled = pd.concat([df_maj, df_min_oversampled])
    X_resampled = df_oversampled.drop('survived', axis=1)
    y_resampled = df_oversampled['survived']
    print("Manual Oversampling executed!")

print(f"Resampled class counts:\n{y_resampled.value_counts()}")