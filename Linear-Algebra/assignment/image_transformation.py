#!/usr/bin/env python

# Import the library
import numpy as np
import matplotlib.pyplot as plt

heart_img = np.array([[255,0,0,255,0,0,255],
              [0,255/2,255/2,0,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
          [0,255/2,255/2,255/2,255/2,255/2,0],
              [255,0,255/2,255/2,255/2,0,255],
                  [255,255,0,255/2,0,255,255],
                  [255,255,255,0,255,255,255]])

# This is a helper function that makes it easy for you to show images!
def show_image(image, name_identifier):
  plt.imshow(image, cmap="gray")
  plt.title(name_identifier)
  plt.show()
  plt.clf()

# Show heart image
show_image(heart_img, "Heart Image")

# Invert color
inverted_heart_img  = 255 - heart_img  
show_image(inverted_heart_img, "Inverted heart_img")

# Rotate heart
rotated_heart_img  = heart_img.T
show_image(rotated_heart_img, "Rotated heart")

# Random Image


# Solve for heart image

