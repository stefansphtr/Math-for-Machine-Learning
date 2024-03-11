#!/usr/bin/env python

# Import library
import numpy as np
import matplotlib.pyplot as plt

def limit_derivative(f, x, h):
    """
    f: function to be differentiated 
    x: the point at which to differentiate f 
    h: distance between the points to be evaluated
    """
    # compute the derivative at x with limit definition
    result = (f(x + h) - f(x)) / h
    return result

# f4(x) = cos(x)
def f4(x):
    return np.cos(x)

# f5(x) = log(x)
def f5(x):
    return np.log(x)

# Modify plot_approx_deriv() to use np.gradient()
def plot_approx_deriv_np_gradient(f):
    x_vals = np.linspace(1, 10, 200)
    y_vals = f(x_vals)
    derivative_values = np.gradient(y_vals, x_vals)
    plt.plot(x_vals, derivative_values, label="np.gradient() Derivative")
    plt.legend()
    plt.title("Derivative using np.gradient()")
    plt.show()

# Change the h_vals and/or x_vals to look at a different range or values
def plot_approx_deriv(f):
    x_vals = np.linspace(0.1, 5, 200)  # Changed range
    h_vals = [0.1, 0.01, 0.001]  # Changed values

    for h in h_vals:
        derivative_values = []
        for x in x_vals:
            derivative_values.append(limit_derivative(f, x, h))
        plt.plot(x_vals, derivative_values, linestyle='--', label="h=" + str(h))
    plt.legend()
    plt.title("Convergence to Derivative by varying h")
    plt.show()

# Compare our method of plot_approx_deriv() to plotting using np.gradient()
print("Using limit definition of derivative:")
plot_approx_deriv(f4)
print("Using np.gradient():")
plot_approx_deriv_np_gradient(f4)

print("Using limit definition of derivative:")
plot_approx_deriv(f5)
print("Using np.gradient():")
plot_approx_deriv_np_gradient(f5)