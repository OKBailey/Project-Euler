from math import sqrt

def is_prime(n):
    flag = 0
    if n > 1:
        for i in range(2,int(sqrt(n)) + 1):
            if n%i == 0:
                flag = 1
                break
        if flag == 0:
            return True
        else:
            return False
    else:
        return False

def ordinal_suffix(n):
    a = str(n)
    if a[-1] == '1':
        return 'st'
    elif a[-1] == '2':
        return 'nd'
    elif a[-1] == '3':
        return 'rd'
    else:
        return 'th'