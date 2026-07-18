# Day 5: CNNs & Image Classification (TensorFlow/Keras)

## Topics covered
- CNN (Convolutional Neural Network) architecture for image data
- Conv2D, MaxPooling2D, Flatten, Dense layers
- ReLU and Softmax activation functions
- Matrix multiplication as the core GPU-accelerated operation
- RNN (concept introduced, not yet coded - for sequential data)
- TensorFlow/Keras vs PyTorch (Day 4) workflow differences
- Dataset auto-downloading via keras.datasets

## What I did
1. Built and trained a CNN on the MNIST handwritten digit dataset
   (28x28 grayscale images, 10 classes). Architecture: 2 Conv2D+Pool
   blocks -> Flatten -> Dense(128) -> Dense(10, softmax).
2. Started loading the CIFAR-10 dataset (32x32 color images, 10 classes)
   - hit a numpy/TensorFlow version conflict, fixed by downgrading numpy
     to <2.0 and reinstalling TensorFlow.

## Key concepts
- Conv2D filters slide over the image detecting patterns (edges ->
  shapes -> objects) - stacking layers builds a feature hierarchy.
- MaxPooling shrinks the image while keeping the strongest signals,
  reducing computation.
- Every Conv2D/Dense operation is matrix multiplication under the hood
  - this is why training runs on the H200 GPU instead of CPU.
- Dataset loaders (`mnist.load_data()`, `cifar10.load_data()`) download
  automatically on first call and cache locally after that.

## Issues faced
- TensorFlow import/compatibility error caused by numpy 2.x - resolved
  with: `pip uninstall numpy` -> `pip install "numpy<2"` -> reinstall
  TensorFlow.

## AI tool disclosure
Used Claude to explain CNN architecture, ReLU/Softmax, matrix
multiplication's role in GPU training, and to debug the numpy/
TensorFlow version conflict, and to structure today's notebook code
into organized script files for the GitHub repo.