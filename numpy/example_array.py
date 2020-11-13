import numpy as np

# Initialization with a range and size, note that the right boundary is closed.
x = np.linspace(0, 1, num=11)
print('x:', x)

# Initialization with linspace, with excluded end point.
x = np.linspace(0, 1, num=10, endpoint=False)
print('x:', x)

# 1D array initialization.
x = np.array([1,2])
print('x:', x)
print('x.shape:', x.shape)

# 1D array is not equivalent to matrix with size of Nx1, i.e., column vector.
# The transposition of 1D array is still 1D array.
print('x.T:', x.T)

# This is a Nx1 matrix, i.e., column vector.
x = np.array([[1],[2]])
print('x.T:', x.T)

A = np.array([[2,0], [0,2], [1,1]])
print('A:\n', A)

# 2D array initialization, with explicit float type.
B = np.array([[1, 2, 3], [4, 5, 6]], np.float)
print(B)

# Element-wise multiplication.
print(A*A)

# Matrix multiplication.
print(A@x)
