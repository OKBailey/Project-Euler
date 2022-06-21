########################################################
########################################################
# NAME:         LEAST COMMON MULTIPLE OF RANGE
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE LEAST COMMON MULTIPLE OF A
#               RANGE OF INTEGERS, WHERE HTE LIMITS OF
#               THE RANGE ARE PARAMETERS.
########################################################
########################################################
from math import gcd

def least_commom_multiple_of_range(low, high):
    lcm = 1
    for i in range(low,high):
        lcm *= i // gcd(i, lcm)
    return lcm

low, high = 1, 20
print(f'The smallest positive number that is evenly divisible by all numbers between {low} and {high} is {least_commom_multiple_of_range(low, high)}.')
