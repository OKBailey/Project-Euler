##########################################################
##########################################################
# NAME:         POWER DIGIT SUM
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE SUM OF DIGITS IN THE NUMBER
#               x^n, WHERE x AND n ARE GIVEN PARAMETERS.
##########################################################
##########################################################

def power_digit_sum(x: int,n: int) -> int:
    num_list = list(str(x**n))
    sum_of_digits = 0
    for num in num_list:
        sum_of_digits += int(num)
    return sum_of_digits

x = 2
n = 1000
digit_sum = power_digit_sum(x,n)
print(f'The sum of the digits in the number {x}^{n} is {digit_sum:,}.')

