from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Values of k
k_values = [1, 3, 5, 7]

accuracies = []

# Calculate accuracy using 10-fold cross validation
for k in k_values:
    model = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(model, X, y, cv=10)

    accuracy = scores.mean()
    accuracies.append(accuracy)

    print("k =", k)
    print("Accuracy =", accuracy)
    print()

# Plot k vs accuracy
plt.plot(k_values, accuracies, marker='o')

plt.xlabel("Value of k")
plt.ylabel("Accuracy")
plt.title("k-NN Accuracy using 10-Fold Cross Validation")
plt.xticks(k_values)
plt.grid()
plt.show()