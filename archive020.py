############################################################
############################################################
# NAME:         NUMBER LETTER COUNTS
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  FOR A GIVEN RANGE OF INTEGERS, THIS CONVERTS
#               EACH INTEGER TO SPELLED-OUT TEXT AND 
#               CALCULATES THE NUMBER OF LETTERS FOR THE
#               ENTIRE RANGE. THIS DOES NOT INCLUDE HYPHENS
#               OR BLANK SPACES.
############################################################
############################################################

# Computes the factorial of a given integer
def fact(n):
    i = n
    result = 1
    while i >= 1:
        result *= i
        i -= 1
    return result

# Computes the sum of digits in the factorial for a given integer
def fact_sum_of_digits(n):
    digit_list = list(str(fact(n)))
    for i, char in enumerate(digit_list):
        digit_list[i] = int(char)
    return sum(digit_list)

num = 100
sum_of_digits = fact_sum_of_digits(num)
print(f'The sum of digits in the number {num}! is {sum_of_digits:,}.')

