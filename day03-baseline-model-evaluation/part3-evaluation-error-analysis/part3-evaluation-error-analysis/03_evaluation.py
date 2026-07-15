"""
Day 3 - Part 3: Evaluation, Error Analysis, Threshold Tuning
Note: run after Part 2 in the same session
(needs baseline_pipeline, X_test, y_test, X_train, y_train).
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay,
    classification_report, roc_auc_score, RocCurveDisplay,
    PrecisionRecallDisplay
)
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)  # only needed here for target_names

# 5. Evaluate the baseline
# class 0 = malignant, class 1 = benign
# We also calculate metrics treating class 0 (malignant) as positive,
# since missing a malignant tumor is the costlier error.
y_pred = baseline_pipeline.predict(X_test)
y_prob_benign = baseline_pipeline.predict_proba(X_test)[:, 1]
y_prob_malignant = baseline_pipeline.predict_proba(X_test)[:, 0]

metrics = {
    "Accuracy": accuracy_score(y_test, y_pred),
    "Precision (benign as positive)": precision_score(y_test, y_pred),
    "Recall (benign as positive)": recall_score(y_test, y_pred),
    "F1 (benign as positive)": f1_score(y_test, y_pred),
    "ROC-AUC": roc_auc_score(y_test, y_prob_benign),
    "Recall for malignant class": recall_score(y_test, y_pred, pos_label=0),
    "Precision for malignant class": precision_score(y_test, y_pred, pos_label=0),
}

metrics_df = pd.DataFrame(metrics.items(), columns=["Metric", "Score"])
print(metrics_df)

print(classification_report(
    y_test,
    y_pred,
    target_names=data.target_names
))

# Confusion matrix, ROC curve, Precision-Recall curve
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=data.target_names,
    cmap="Blues"
)
plt.title("Baseline Confusion Matrix")
plt.show()

RocCurveDisplay.from_predictions(y_test, y_prob_benign)
plt.title("Baseline ROC Curve")
plt.show()

PrecisionRecallDisplay.from_predictions(y_test, y_prob_benign)
plt.title("Baseline Precision-Recall Curve")
plt.show()

# 6. Error analysis - which samples got misclassified, and why
error_df = X_test.copy()
error_df["actual"] = y_test
error_df["predicted"] = y_pred
error_df["probability_benign"] = y_prob_benign
error_df["correct"] = error_df["actual"] == error_df["predicted"]

errors = error_df.loc[~error_df["correct"]].copy()
errors["actual_name"] = errors["actual"].map({0: "malignant", 1: "benign"})
errors["predicted_name"] = errors["predicted"].map({0: "malignant", 1: "benign"})

print("Number of misclassified samples:", len(errors))
print(
    errors[
        ["actual_name", "predicted_name", "probability_benign",
         "mean radius", "mean texture", "mean area"]
    ].sort_values("probability_benign")
)

# 7. Student activity: change the decision threshold
# Default threshold is 0.5. Lowering it catches more malignant cases (higher recall)
# at the cost of more false alarms (lower precision) - relevant in high-risk domains.
threshold_results = []

for threshold in [0.30, 0.40, 0.50, 0.60, 0.70]:
    # Predict benign when P(benign) >= threshold
    threshold_pred = (y_prob_benign >= threshold).astype(int)
    threshold_results.append({
        "threshold": threshold,
        "accuracy": accuracy_score(y_test, threshold_pred),
        "malignant_recall": recall_score(y_test, threshold_pred, pos_label=0),
        "malignant_precision": precision_score(y_test, threshold_pred, pos_label=0),
        "f1_macro": f1_score(y_test, threshold_pred, average="macro")
    })

threshold_df = pd.DataFrame(threshold_results)
print(threshold_df.to_string(index=False))