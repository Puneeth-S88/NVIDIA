"""
Day 6 - Part 4: Custom Classifier Head on Frozen Transformer Embeddings
Simulates the transfer-learning pattern: pretrained transformer
produces embeddings (frozen, not retrained), then a small classifier
(Logistic Regression) is trained on top of those embeddings.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def execute_custom_classifier_training():
    """
    Combines frozen high-dimensional Transformer context embeddings
    with a distinct downstream classifier head to create a hybrid model.
    """
    print("Simulating upstream extraction step...")

    # Generate mock transformer embeddings (768 = DistilBERT hidden size)
    np.random.seed(42)
    mock_transformer_embeddings = np.random.randn(100, 768)

    # Generate binary labels
    mock_labels = np.random.randint(0, 2, size=(100,))

    X_train, X_test, y_train, y_test = train_test_split(
        mock_transformer_embeddings,
        mock_labels,
        test_size=0.2,
        random_state=42
    )

    custom_head = LogisticRegression(
        C=1.0,
        max_iter=1000,
        solver='lbfgs'
    )

    custom_head.fit(X_train, y_train)

    predictions = custom_head.predict(X_test)
    prediction_probabilities = custom_head.predict_proba(X_test)[:, 1]

    print(f"Custom classifier trained on {X_train.shape[0]} samples.")
    print(f"Prediction array shape: {predictions.shape}")

    return y_test, predictions, prediction_probabilities


if __name__ == "__main__":
    y_true, y_pred, y_prob = execute_custom_classifier_training()