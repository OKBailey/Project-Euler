##########################################################
##########################################################
# NAME:         LONGEST COLLATZ SEQUENCE
# AUTHOR:       SCOTT BAILEY
# DESCRIPTION:  RETURNS THE STARTING VALUE AND NUMBER OF
#               ITEMS IN THE SEQUENCE FOR THE LONGEST
#               COLLATZ SEQUENCE WITH STARTING VALUES
#               LESS THAN N, WHERE N IS A GIVEN PARAMETER.
#
#               ELEMENTS OF A COLLATZ SEQUENCE ARE GIVEN
#               BY:
#                   X --> X / 2 (IF X IS EVEN)
#                   X --> 3X + 1 (IF X IS ODD)
##########################################################
##########################################################
def collatz_sequence(n):
    collatz = [n]
    temp = n
    # added 2nd condition to allow for n=1
    while (temp != 1) or (len(collatz) == 1):
        if temp % 2 == 0:
            temp /= 2
        else:
            temp = 3*temp + 1
        collatz.append(int(temp))
    return collatz

def longest_collatz_seed(lim):
    collatz_dict = {}
    i = 1
    while i < lim:
        collatz_length = len(collatz_sequence(i))
        collatz_dict[collatz_length] = i
        i += 1
    return [collatz_dict[max(collatz_dict)], max(collatz_dict)]

limit = 1000000
longest = longest_collatz_seed(limit)
print(f'The longest Collatz sequence for starting values under {limit:,} is obtained with a starting value of {longest[0]:,}. The sequence contains {longest[1]:,} values.')

