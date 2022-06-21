#########################################################
#########################################################
# NAME:         SUM OF SQUARES DIFFERENCE
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE DIFFERENCE BETWEEN THE SQUARE
#               OF THE SUM OF THE FIRST N NATURAL NUMBERS
#               AND THE SUM OF THE SQUARES OF THE FIRST
#               N NATURAL NUMBERS, WHERE N IS A GIVEN
#               PARAMETER.
#########################################################
#########################################################

def sum_of_square(n):
    i = 1
    ans = 0
    while i <= n:
        ans += i**2
        i += 1
    return ans

def square_of_sum(n):
    i = 1
    ans = 0
    while i <= n:
        ans += i
        i += 1
    return ans**2

def diff_between_squares_and_sums(n):
    a = square_of_sum(n) - sum_of_square(n)
    return a

lim = 100
diff = diff_between_squares_and_sums(lim)
print(f'The difference between the square of the sum and the sum of the squares of the first {lim} natural numbers is {diff}.')