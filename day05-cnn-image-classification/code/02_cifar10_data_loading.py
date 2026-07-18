"""
Day 5 - Part 2: CIFAR-10 Dataset Loading
CIFAR-10 = 60,000 32x32 color images across 10 classes
(airplane, car, bird, cat, deer, dog, frog, horse, ship, truck).

NOTE: If TensorFlow throws a numpy compatibility error, run these
commands in your terminal (not this script) first, then restart
the kernel/session before rerunning this file:

    pip uninstall -y numpy
    pip install "numpy<2" --break-system-packages
    pip install --upgrade tensorflow --break-system-packages
"""
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

# Load CIFAR-10 dataset (auto-downloads on first run, then cached)
(X_train, y_train), (X_test, y_test) = datasets.cifar10.load_data()

print("Training data shape:", X_train.shape)   # (50000, 32, 32, 3)
print("Test data shape:", X_test.shape)        # (10000, 32, 32, 3)
print("Number of classes:", len(np.unique(y_train)))

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Preview a few sample images
plt.figure(figsize=(8, 8))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(X_train[i])
    plt.title(class_names[int(y_train[i])])
    plt.axis('off')
plt.tight_layout()
plt.show()