#!/usr/bin/env python

"""
Study Cases:

Out of a sample of 100 shoppers who visit a website, 23 people bought something. 
Suppose we are running a hypothesis test for this sample with the following null and alternative hypotheses:

Null hypothesis: 20% of shoppers who visit the website buy something

Alternative hypothesis: More than 20% of shoppers who visit the website buy something

Write a program in Python to run a one-sided binomial hypothesis test and save it 
in a variable called p_value. 

Print out p_value. What is your conclusion based on the result?
"""

# Answer

"""
Define the value we have:
k = 23
n = 100
p = 0.20
"""


# Import library
from scipy.stats import binomtest
