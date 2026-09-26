import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.spatial.distance import cdist

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# Try different values of K
k_values = [2, 3, 4, 5]

for k in k_values:

    # K-means using Euclidean distance
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    model.fit(X_train)

    # Predict clusters for test data
    test_clusters = model.predict(X_test)

    # Match each cluster with the most common actual class
    cluster_to_class = {}

    for cluster in range(k):
        classes = y_train[model.labels_ == cluster]

        if len(classes) > 0:
            cluster_to_class[cluster] = np.bincount(classes).argmax()

    y_pred = np.array([
        cluster_to_class.get(cluster, 0)
        for cluster in test_clusters
    ])

    accuracy = accuracy_score(y_test, y_pred)

    print("K =", k)
    print("Distance Measure = Euclidean")
    print("Accuracy =", accuracy)
    print()