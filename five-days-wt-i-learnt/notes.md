# 5-Day Recap — Topics Covered

## Day 1: Environment Setup & Infrastructure
- What a GPU is and why AI needs it (H200: 141GB HBM3e memory, Transformer Engine)
- SSH into the DGX/lab machine (`ssh username@IP`)
- Kubernetes basics: Pods, `pod.yaml` manifests, `kubectl apply`, `kubectl get pods/services`
- Accessing a running container: `kubectl exec -it <pod/service> -- bash`
- Launching JupyterHub from inside the container
- Session cleanup: stopping Jupyter (`Ctrl+C`), exiting the container, `kubectl delete pod`
- Why local container storage wipes daily — need to push work to GitHub before session ends

## Day 2: ML Fundamentals (Titanic Dataset — Full Pipeline)
- Data loading (CSV/GitHub, Seaborn, sklearn built-ins)
- Data cleaning: handling missing values, duplicates
- EDA & outlier detection: boxplots, IQR method, Z-score method
- Visualization: countplots, barplots, KDE plots, correlation heatmaps
- Feature engineering (creating new columns like `family_size`, `is_alone`)
- Encoding categoricals: Label Encoding, One-Hot Encoding, Ordinal mapping
- Feature scaling: StandardScaler, MinMaxScaler, RobustScaler
- Feature selection: SelectKBest, RFE
- Dimensionality reduction: PCA
- Train/test split, K-Fold cross-validation
- Handling class imbalance: SMOTE
- Regression models: Linear, Polynomial, Decision Tree, Random Forest
- Classification models: Logistic Regression, KNN, Decision Tree, Random Forest, SVM, Naive Bayes
- Clustering: K-Means (elbow method), Agglomerative, DBSCAN
- Model evaluation: accuracy/precision/recall/F1, confusion matrix, ROC curves

## Day 3: Baseline Models, Evaluation & ML Pipelines (Breast Cancer Dataset)
- **Regression vs Classification** — core distinction (continuous number vs category)
- Leakage-safe train/test splitting (stratified)
- `sklearn.Pipeline` — bundling preprocessing + model so scaling only fits on training data
- Baseline model: Logistic Regression
- Evaluation metrics in a real-world context: precision/recall tradeoffs, why "positive class" choice matters (e.g., malignant vs benign)
- ROC-AUC and Precision-Recall curves
- Error analysis — manually inspecting misclassified samples
- Decision threshold tuning (moving away from default 0.5) to balance false positives vs false negatives

## Day 4: Neural Networks & PyTorch Fundamentals
- The neuron: weights, bias, activation — same math as logistic regression, just building blocks
- Layers: input, hidden, output; "deep learning" = many hidden layers
- Activation functions: ReLU, Sigmoid, Softmax — why non-linearity matters
- The training loop: forward pass → loss function → backpropagation → gradient descent
- Epochs, loss convergence
- PyTorch basics: `nn.Linear`, `nn.Module`, `MSELoss`, `BCELoss`, `CrossEntropyLoss`
- Optimizers: SGD vs Adam (adaptive learning rates)
- Dropout — regularization to prevent overfitting
- Building custom layers (`nn.Parameter`, subclassing `nn.Module`)
- Learning rate schedulers (`StepLR`) — decaying learning rate over epochs

## Day 5: CNNs & Image Classification (TensorFlow/Keras)
- Why images need CNNs instead of plain dense networks (preserving spatial structure)
- Conv2D — filters/kernels detecting patterns (edges → shapes → objects)
- MaxPooling — downsampling while keeping strongest signals
- Flatten + Dense layers for final classification
- Matrix multiplication as the core operation — why this needs the GPU
- RNNs (introduced conceptually) — for sequential data like text/time series
- TensorFlow/Keras workflow (`model.fit()`) vs PyTorch's manual training loop
- Dataset auto-downloading (MNIST, CIFAR-10) via `keras.datasets`
- Debugging real dependency conflicts (numpy/TensorFlow version mismatch)

---

**Pattern across the week:** Day 1 was infrastructure, Day 2–3 built your classical ML foundation (the "old" way models learn), and Day 4–5 shifted into deep learning (the "new" way — networks that learn their own features). Week 2 of your program (per the offer letter) moves into Transformers, LLM fine-tuning (LoRA), and Generative AI — which will build directly on the neural network foundation from Days 4–5.