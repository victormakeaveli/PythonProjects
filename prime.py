from math import sqrt


def is_prime(n):
    if n % 2 == 0 and n > 1:
        return False
    if n % (int(sqrt(n))) == 0:
        return False
    else:
        return True
