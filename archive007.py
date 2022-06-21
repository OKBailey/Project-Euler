########################################################
########################################################
# NAME:         NTH PRIME NUMBER
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE NTH PRIME NUMBER, WHERE N
#               IS A GIVEN PARAMETER.
########################################################
########################################################

from common_funcs import *

def nth_prime(n):
    prime_list = []
    i = 1
    while len(prime_list) < n:
        if is_prime(i) == True:
            prime_list.append(i)
        i += 1
    return max(prime_list)

n = 10001
print(f'The {n:,}{ordinal_suffix(n)} prime number is {nth_prime(n):,}.')