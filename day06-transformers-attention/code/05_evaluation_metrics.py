"""
Day 6 - Part 5: Manual Evaluation Metrics (TP, TN, FP, FN, Precision,
Recall, F1, Accuracy) computed from scratch using NumPy.
"""
import numpy as np


def calculate_professional_metrics(true_labels, predicted_labels):
    """
    Computes Precision, Recall, F1-Score, and Accuracy
    from true and predicted labels.
    """
    y_true = np.array(true_labels)
    y_pred = np.array(predicted_labels)

    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tn = np.sum((y_true == 0) & (y_pred == 0))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1_score = (
        2 * (precision * recall) / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )
    accuracy = (tp + tn) / len(y_true)

    print("========== MACHINE LEARNING REPORT ==========")
    print(f"True Positives : {tp}")
    print(f"False Positives: {fp}")
    print(f"True Negatives : {tn}")
    print(f"False Negatives: {fn}")
    print("---------------------------------------------")
    print(f"Precision : {precision * 100:.2f}%")
    print(f"Recall    : {recall * 100:.2f}%")
    print(f"F1-Score  : {f1_score * 100:.2f}%")
    print(f"Accuracy  : {accuracy * 100:.2f}%")
    print("=============================================")

    return {
        "precision": precision,
        "recall": recall,
        "f1": f1_score,
        "accuracy": accuracy
    }


if __name__ == "__main__":
    target_ground_truth = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
    model_predictions = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]

    metrics = calculate_professional_metrics(
        target_ground_truth,
        model_predictions
    )