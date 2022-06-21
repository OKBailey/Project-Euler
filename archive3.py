########################################################
########################################################
# NAME:         LARGEST PRIME FACTOR
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE LARGEST PRIME FACTOR OF A
#               GIVEN NUMBER.
########################################################
########################################################

from math import sqrt
from common_funcs import is_prime

def largest_prime_factor(n):
    prime_fact = [i for i in range(1, int(sqrt(x)) + 1) if (is_prime(i) == True) and (n%i == 0)]
    return max(prime_fact)

x = 600851475143
print(f'The largest prime factor of {x} is {largest_prime_factor(x)}.')