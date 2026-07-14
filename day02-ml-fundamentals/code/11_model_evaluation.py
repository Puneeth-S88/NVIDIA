"""
Day 2 - Step 11: Model Evaluation
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, roc_auc_score,
)

classifiers = {
    'Logistic Regression': (log_clf, X_test_scaled),
    'K-Nearest Neighbors': (knn_clf, X_test_scaled),
    'Decision Tree': (dt_clf, X_test),
    'Random Forest': (rf_clf, X_test),
    'Support Vector Machine': (svm_clf, X_test_scaled),
    'Naive Bayes': (nb_clf, X_test)
}

print("=== Classification Performance Metrics ===")
clf_results = []
for name, (model, data) in classifiers.items():
    preds = model.predict(data)
    acc = accuracy_score(y_test, preds)
    prec = precision_score(y_test, preds)
    rec = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)

    clf_results.append({
        'Model': name,
        'Accuracy': round(acc, 4),
        'Precision': round(prec, 4),
        'Recall': round(rec, 4),
        'F1-Score': round(f1, 4)
    })

print(pd.DataFrame(clf_results))

# 1. Confusion Matrix for Random Forest Classifier
cm = confusion_matrix(y_test, rf_clf.predict(X_test))
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Not Survived', 'Survived'],
            yticklabels=['Not Survived', 'Survived'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix: Random Forest')
plt.show()

# 2. ROC curves for all classifiers
plt.figure(figsize=(10, 8))
for name, (model, data) in classifiers.items():
    probs = model.predict_proba(data)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, probs)
    auc = roc_auc_score(y_test, probs)
    plt.plot(fpr, tpr, label=f"{name} (AUC = {auc:.3f})")

plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curves')
plt.legend()
plt.show()