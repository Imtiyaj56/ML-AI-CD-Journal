import numpy as np
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Overall mean
overall_mean = np.mean(X, axis=0)

# Initialize scatter matrices
within_class_scatter = np.zeros((4, 4))
between_class_scatter = np.zeros((4, 4))

# Calculate within-class and between-class scatter
for class_value in np.unique(y):
    class_data = X[y == class_value]

    # Mean of the class
    class_mean = np.mean(class_data, axis=0)

    # Within-class scatter
    for x in class_data:
        diff = (x - class_mean).reshape(4, 1)
        within_class_scatter += np.dot(diff, diff.T)

    # Between-class scatter
    n = len(class_data)
    diff = (class_mean - overall_mean).reshape(4, 1)
    between_class_scatter += n * np.dot(diff, diff.T)

# Total scatter
total_scatter = np.zeros((4, 4))

for x in X:
    diff = (x - overall_mean).reshape(4, 1)
    total_scatter += np.dot(diff, diff.T)

# Print results
print("Within Class Scatter:")
print(within_class_scatter)

print("\nBetween Class Scatter:")
print(between_class_scatter)

print("\nTotal Scatter:")
print(total_scatter)

# Verify relationship
print("\nWithin + Between = Total:")
print(np.allclose(within_class_scatter + between_class_scatter, total_scatter))