"""
Day 3 - Part 2: Train/Test Split + Preprocessing Pipeline + Baseline Model
Note: run after Part 1 in the same session (needs X, y, SEED).
"""
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# 3. Create a leakage-safe train/test split
# Stratify keeps class proportions similar in train and test sets.
# Test set stays untouched until final evaluation.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    stratify=y,
    random_state=SEED
)

print("Training samples:", len(X_train))
print("Test samples:", len(X_test))
print("\nTraining class proportions:")
print(y_train.value_counts(normalize=True).sort_index().to_frame("proportion"))

# 4. Build a preprocessing + modeling pipeline
# Scaler is fitted ONLY on training data (it's inside the pipeline) -> prevents data leakage
baseline_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=2000, random_state=SEED))
])

baseline_pipeline.fit(X_train, y_train)
print("Baseline model trained.")