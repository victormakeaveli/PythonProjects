from math import sqrt

numbers = ()
a = list(map(lambda n: f'{n} true' if n % (int(sqrt(n))) != 0 else f'{n} false', (i for i in range(1, 19))))
print(a)
