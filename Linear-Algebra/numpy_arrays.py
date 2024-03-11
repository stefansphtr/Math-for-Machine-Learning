#!/usr/bin/env python

import numpy as np

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
