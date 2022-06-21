########################################################
########################################################
# NAME:         MULTIPLES OF 3 OR 5
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE SUM OF MULTIPLES OF 3 OR 5
#               FOR A SPECIFIED INTEGER
########################################################
########################################################

def sum_of_multiples(max_factor):
    multiple_list = [i for i in range(1,max_factor) if (i%3==0) or (i%5==0)]
    sum_of_multiple_list = sum(multiple_list)
    return sum_of_multiple_list

max_fact = 1000
print(sum_of_multiples(max_fact))
