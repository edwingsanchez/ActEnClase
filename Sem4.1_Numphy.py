import numpy as np



# Create arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
print(arr1 + 10)
print(arr1 * 2)
print(np.sqrt(arr1))

# Matrix operations
print(np.dot(arr2, arr2.T))

# Statistical functions
print(np.mean(arr1))
print(np.std(arr1))
print(np.sum(arr1))

# Useful functions
linspace = np.linspace(0, 10, 5)  # 5 equally spaced values
arange = np.arange(0, 10, 2)  # values from 0 to 10 step 2
zeros = np.zeros((3, 3))  # 3x3 matrix of zeros
ones = np.ones((2, 4))  # 2x4 matrix of ones