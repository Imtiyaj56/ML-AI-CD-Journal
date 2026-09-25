import statistics

X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2]

X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2000]

X3 = [1, 2, 3, 10, 20, 30, 100, 200, 300, 1000, 2000, 3000]

print("X1")
print("Standard Deviation:", statistics.pstdev(X1))
print("Variance:", statistics.pvariance(X1))

print("\nX2")
print("Standard Deviation:", statistics.pstdev(X2))
print("Variance:", statistics.pvariance(X2))

print("\nX3")
print("Standard Deviation:", statistics.pstdev(X3))
print("Variance:", statistics.pvariance(X3))