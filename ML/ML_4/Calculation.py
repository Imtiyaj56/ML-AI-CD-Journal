# Calculate Cosine Similarity and Euclidean Distance

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import euclidean

A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = np.array([1, 3, 5, 7, 9, 7, 5, 3, 1, 0])

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([1, 3, 5, 7, 9, 7, 5, 3, 1, 0])

# Cosine Similarity
cos_AB = cosine_similarity([A], [B])[0][0]
cos_XY = cosine_similarity([X], [Y])[0][0]

# Euclidean Distance
euclidean_AB = euclidean(A, B)
euclidean_XY = euclidean(X, Y)

print("Cosine Similarity")
print("(A, B):", cos_AB)
print("(X, Y):", cos_XY)

print("\nEuclidean Distance")
print("(A, B):", euclidean_AB)
print("(X, Y):", euclidean_XY)