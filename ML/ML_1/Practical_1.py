import statistics

X1 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2]

X2 = [1, 2, 3, 4, 5, 4, 3, 2, 4, 5, 1, 2, 3, 4, 2, 5, 1, 3, 2, 1, 2, 1, 1, 1, 2000]

X3 = [1, 2, 3, 10, 20, 30, 100, 200, 300, 1000, 2000, 3000]

print("X1")
print("Mean:", statistics.mean(X1))
print("Median:", statistics.median(X1))
print("Mode:", statistics.mode(X1))

print("\nX2")
print("Mean:", statistics.mean(X2))
print("Median:", statistics.median(X2))
print("Mode:", statistics.mode(X2))

print("\nX3")
print("Mean:", statistics.mean(X3))
print("Median:", statistics.median(X3))
print("Mode:", statistics.multimode(X3))