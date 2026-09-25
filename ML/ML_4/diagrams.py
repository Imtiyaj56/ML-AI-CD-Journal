# Geometrical diagram for Cosine Similarity and Euclidean Distance

import numpy as np
import matplotlib.pyplot as plt

A = np.array([1, 2])
B = np.array([4, 5])

plt.figure(figsize=(7, 6))

# Vectors
plt.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy',
           scale=1, label='Vector A')

plt.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy',
           scale=1, label='Vector B')

# Points
plt.scatter(A[0], A[1])
plt.scatter(B[0], B[1])

plt.text(A[0], A[1], ' A')
plt.text(B[0], B[1], ' B')

plt.xlim(0, 6)
plt.ylim(0, 7)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Cosine Similarity and Euclidean Distance')
plt.grid()
plt.legend()

plt.show()