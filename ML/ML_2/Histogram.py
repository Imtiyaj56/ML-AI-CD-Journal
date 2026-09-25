import matplotlib.pyplot as plt
import statistics

X = [1, 3, 2, 4, 56, 4, 3, 2, 4, 5, 3, 1, 2, 3, 2, 3, 1, 4]

sd = statistics.pstdev(X)
variance = statistics.pvariance(X)
mean = statistics.mean(X)

plt.hist(X, bins=10, edgecolor='black')

plt.axvline(mean, linestyle='--', label='Mean')
plt.axvline(mean + sd, linestyle=':', label='Mean + SD')
plt.axvline(mean - sd, linestyle=':', label='Mean - SD')

plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram with Standard Deviation and Variance')
plt.legend()

plt.show()

print("Standard Deviation:", sd)
print("Variance:", variance)