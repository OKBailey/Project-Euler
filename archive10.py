########################################################
########################################################
# NAME:         SUM OF PRIMES
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE SUM OF PRIME NUMBERS BELOW
#               N, WHERE N IS A GIVEN PARAMETER.
########################################################
########################################################

from common_funcs import is_prime

n = 2000000

def sum_of_primes(lim):
    i = 1
    primes = []
    while i < lim:
        if is_prime(i) == True:
            primes.append(i)
        i += 1
    return sum(primes)

print(f'The sum of primes below {n:,} is {sum_of_primes(n):,}.')