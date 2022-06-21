########################################################
########################################################
# NAME:         EVEN FIBONACCI NUMBERS
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE SUM OF OF EVEN FIBONACCI
#               NUMBERS THAT ARE BELOW A SPECIFIED
#               LIMIT
########################################################
########################################################

### INCOMPLETE ###

def sum_of_even_fibs(limit):
    fibs = [1, 2]
    i = 0
    while i < limit - 2:
        fibs.append(fibs[i] + fibs[i+1])
        i += 1
    even_fibs = [j for j in fibs if j%2 == 0]
    return fibs

lim = 10
print(sum_of_even_fibs(lim))