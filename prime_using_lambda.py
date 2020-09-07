from math import sqrt

a = list(map(lambda n:
                 f'{n} is prime' if n % (int(sqrt(n))) != 0 
            else f'{n} is not prime',
                                 (i for i in range(1, 9999999)
                                 )                        
            )
        )
print(a)