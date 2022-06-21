########################################################
########################################################
# NAME:         LARGEST PALINDROM PRODUCT
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE LARGEST PALINDROME OF THE
#               PRODUCT OF 2 NUMBERS. THE FIRST NUMBER
#               CONTAINS M DIGITS AND THE SECOND NUMBER
#               CONTAINS N DIGITS, WHERE M AND N ARE
#               SPECIFIED PARAMETERS.
########################################################
########################################################

def is_palindrome(n):
    str_n = str(n)
    rev_n = ''.join(reversed(str_n))
    if str_n == rev_n:
        return True
    else:
        return False

def max_palindrome(m, n):
    pal_list = [i * j for j in range(1,10**n) for i in range(1,10**m) if is_palindrome(i * j) == True ]
    max_pal = max(pal_list)
    return max_pal

m = 3
n = 3
print(f'The largest palindrome that is the product of a {m}-digit number and a {n}-digit number is {max_palindrome(m,n)}.')