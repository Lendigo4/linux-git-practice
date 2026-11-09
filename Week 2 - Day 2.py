import numpy as np

# 1. Create a NumPy array of 10 zeros
zeros_arr = np.zeros(10)
print(zeros_arr)

# 2. Create a NumPy array of 10 ones
ones_arr = np.ones(10)
print(ones_arr)

# 3. Generate an array of integers from 1 to 50
arr_50 = np.arange(1, 51)
print(arr_50)

# 4. Reshape a 1D array to 2D (e.g., 3x4)
arr_2d = np.arange(12).reshape(3, 4)
print(arr_2d)

# 5. Find the maximum and minimum values in an array
print("Max value:", arr_50.max())
print("Min value:", arr_50.min())

# 6. Calculate mean, median, and standard deviation
print("Mean:", np.mean(arr_50))
print("Median:", np.median(arr_50))
print("Standard Deviation:", np.std(arr_50))

# 7. Create a 3x3 identity matrix
identity = np.eye(3)
print("3x3 Identity Matrix:\n", identity)

# 8. Replace all negative numbers with zero in an array
arr_neg = np.array([-5, 2, -1, 9, 0, -3])
arr_neg[arr_neg < 0] = 0
print("Negatives replaced with zero:", arr_neg)

# 9. Filter all elements greater than 20
filtered = arr_50[arr_50 > 20]
print("Elements greater than 20:", filtered)

# 10. Add and multiply two arrays element-wise
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Element-wise Addition:", a + b)
print("Element-wise Multiplication:", a * b)

# 11. Stack two arrays vertically
stacked = np.vstack((a, b))
print("Vertically Stacked Arrays:\n", stacked)