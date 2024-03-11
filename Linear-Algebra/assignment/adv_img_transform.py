#!/usr/bin/env python

# Import the library
import numpy as np
import matplotlib.pyplot as plt

# Create a new shape with a NumPy array
new_shape = np.array([[255, 255, 0, 0, 255, 255, 0],
                      [255, 0, 0, 255, 0, 0, 255],
                      [0, 0, 255, 255, 255, 0, 0],
                      [0, 255, 255, 255, 255, 255, 0],
                      [255, 0, 0, 255, 0, 0, 255],
                      [255, 255, 0, 0, 255, 255, 0],
                      [0, 0, 255, 255, 255, 0, 0]])

# Transform image with a permutation matrix
identity_matrix = np.eye(7)

# Shift the columns to the right to create a permutation matrix
perm_matrix = np.roll(identity_matrix, shift= 1, axis= 1)

transformed_image = np.dot(new_shape, perm_matrix)

# This is a helper function that makes it easy for you to show images!
def show_image(image, name_identifier, cmap="gray"):
  plt.imshow(image, cmap=cmap)
  plt.title(name_identifier)
  plt.show()
  plt.clf()

# Show original image
show_image(new_shape, "Original Image")

# Show transformed image
show_image(transformed_image, "Transformed Image")

# Change the color scheme from grayscale. Check the cmap parameter of the imshow() function.
show_image(transformed_image, "Transformed Image - Color", "hot")

# Create a complicated image with more pixels and/or a shape that is not a square matrix.
complicated_image = np.random.randint(0, 255, (10, 15))
show_image(complicated_image, "Complicated Image", "viridis")