#!/usr/bin/env python

import numpy as np

"""
Part 1 - Build Matrix

# Given vectors
vector_1 = np.array([-2,-6,2,3])
vector_2 = np.array([4,1,-3,8])
vector_3 = np.array([5,-7,9,0])

# Define the matrix
matrix = np.column_stack([vector_1, vector_2, vector_3])
print(matrix)

# Print the dimensionality of matrix
print(matrix.shape)

# Print out the third column
print(matrix[:, 2])

# Print out the second column
print(matrix[:, 1])

# Print out the third row
print(matrix[2:3, :])

# Print out the second row
print(matrix[1:2, :])

"""

"""
Part 2 - Matrix Multiplication

# Given
# 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])
# 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])
# 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])

# Calculate D = 4A - 2B
D = (4 * A) - (2 * B)
print(D)

# Calculate E = AC
E = np.matmul(A, C)
print(E)

# Calculate F = CA
F = C@A
print(F)
"""

"""
Part 3 - Special Matrix (Identity, Zeros, and Transpose)

# Given
A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])

AB = A@B
BA = B@A

print(AB)
print(BA)

A_transpose = A.T
B_transpose = B.T

print(A_transpose)
print(B_transpose)
"""

"""
Part 4 - Additional LinAlg Operations

# Represent the following system in NumPy matrix/vector form, then solve for x, y, and z

# Given
'''
4x + z = 2
-y + 2z - 3x = 0
.5y - x - 1.5z = -4
'''

# Define the matrix
A = np.array([
    [4, 0, 1],
    [-3, -1, 2],
    [-1, 0.5, -1.5]
])

# Define the solution of the matrix
b = np.array([2, 0, -4])

# Get the x, y, and z solution
x, y, z = np.linalg.solve(A, b)

print((x, y, z))
"""

