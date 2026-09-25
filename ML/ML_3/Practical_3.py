import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target

# Standardize the data
X = StandardScaler().fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Plot the three classes
plt.figure(figsize=(8, 6))

plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], label="Setosa")
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], label="Versicolor")
plt.scatter(X_pca[y == 2, 0], X_pca[y == 2, 1], label="Virginica")

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA of Iris Dataset")
plt.legend()
plt.grid()

plt.show(block=True)