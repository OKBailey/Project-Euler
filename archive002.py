########################################################
########################################################
# NAME:         EVEN FIBONACCI NUMBERS
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE SUM OF OF EVEN FIBONACCI
#               NUMBERS THAT ARE BELOW A SPECIFIED
#               LIMIT.
########################################################
########################################################

def even_fibonacci_sum(limit):
    seq = [1, 2]
    while seq[-1] + seq[-2] <= limit:
        seq.append(seq[-1] + seq[-2])
    even_fibs = [i for i in seq if i%2 == 0]
    return sum(even_fibs)
    
lim = 4000000
tot = even_fibonacci_sum(lim)
print(f'The sum of the even terms below {lim:,} in a Fibonacci sequence is {tot:,}.')