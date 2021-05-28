from math import sqrt

# a simple variable holding a list with the results of the lambda expression using map 
foo = list(map(lambda n:
                 f'{n} is not prime' if n % (int(sqrt(n))) == 0 or n % 2 == 0
            else f'{n} is prime',
                                 (i for i in range(3, 32)   
                                 )                        
            )
        )
