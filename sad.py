# A happy number is a number which the sum of its square root is equal to 1. 
# The simplest example is the number 10. 
# 10² = 100
# 1² + 0² + 0² = 1, happy

# Another example is the number 7.
# 7² = 49
# 4² + 9² = 97
# 9² + 7² = 130
# 1² + 3² + 0² = 10
# 1² + 0² = 1, happy

# I created a function that takes n numbers and it checks if it fits a happy number or not. No biggie at all. At the time I developed some kind of "save" that stores every result, so everytime the stored number appears, it triggers the previous result preventing the cpu to do the same math over and over.

def sad():

    positive_results = []
    negative_results = []
    happy_numbers = []
    sad_numbers = []

    global inp_number
    global its

    for inp_number in range(1, 33): # ¹ #
        # this variable makes the desired number to-be-tested, a list, so I can iterate over the number.
        number = [int(i) for i in str(inp_number)]
        # check is a variable which, self-explanatorily, checks, if it arrived at the target result, I had to define it here out of the loop so the loop itself could work.
        check = 0
        # counter
        counter = 0

        while check != 1:

            counter += 1
            # it goes like this: if the length of the list-number to-be-tested is equal to N then the appropriate logic its applied(I couldn't think of any other better way to do this)
            if len(number) == 1:
                # check is now the result of the math behind it all
                check = (number[0] ** 2)
                # some output
                print(f'[1] Checking {inp_number} > {number[0]}² = {check}')

            elif len(number) == 2:
                check = (number[0] ** 2) + (number[1] ** 2)
                print(f'[2] Checking {inp_number} > {number[0]}² + {number[1]}² = {check}')

            elif len(number) == 3:
                check = (number[0] ** 2) + (number[1] ** 2) + (number[2] ** 2)
                print(f'[3] Checking {inp_number} > {number[0]}² + {number[1]}² + {number[2]}² = {check}')

            elif len(number) == 4:
                check = (number[0] ** 2) + (number[1] ** 2) + (number[2] ** 2) + (number[3] ** 2)
                print(f'[4] Checking {inp_number} > {number[0]}² + {number[1]}² + {number[2]}² + {number[3]} = {check}')

            elif len(number) == 5:
                check = (number[0] ** 2) + (number[1] ** 2) + (number[2] ** 2) + (number[3] ** 2) + (number[4] ** 2)
                print(f'[5] Checking {inp_number} > {number[0]}² + {number[1]}² + {number[2]}² + {number[3]}² + {number[4]}² = {check}')

            else:
                print('error')
            # for the code to work properly I have to redefine the variable holding the result, not every number has its result defined on the first loop.
            number = [int(i) for i in str(check)]

            # now, my Rembrandt 
            # before storing the result, it sees if its already there, in the positive results, the ones that passed.
            if check in positive_results:
                its = True
                break
            # it gets trickier here. If the code is here then it means the result is not in the positive results, now it checks if its not in the negative results, which firstly(at the beginning of the numbers to-be-tested FOR loop¹) every number will not be. Then it checks if the check variable is at the target result so it can move on, otherwise the check variable will be appended to the negative_results list, doing the purpose of this whole statement.
            if check not in negative_results:
                if check == 1: # ² #
                    pass
                else:
                    negative_results.append(check)
                    continue
            # if the above is appended to the negative_results list, it means the number is not happy, therefore:
            else:
                # it gets stated so.
                its = False
                # appended to the designated list
                sad_numbers.append(inp_number)
                # and break the loop
                break
            # if the ², then it gets stated so. (the final 'check', per say)
            its = True
        # the final check is stated, now it is appended respectively
        if its:
            happy_numbers.append(inp_number)
            print(f'{inp_number} is happy')
            print()
            # all cool and nice but the result has to go somewhere, so
            # if its already here it means its a happy number, now it needs to be appended to the positive_results, removing it from the negative ones, for that, it checks beforehand if the number is already on both lists.
            while counter != 1:
                # this counter variable being used to make sure that the code had run at the loop first, otherwise it doesn't need to be stored
                counter -= 1
                # if there's already an i stored then skip it
                if any(i in negative_results for i in positive_results):
                    pass
                else: # otherwise it does it's thing
                    positive_results.append(negative_results[-1])
                negative_results.pop()
            continue
        
        else:
            print(f'{inp_number} is sad')
            print()

    # some output
    print('-'*200)
    print(f'Happy {len(happy_numbers)} => {happy_numbers}')
    print(f'Sad {len(sad_numbers)} => {sad_numbers}')
    print('-'*200)
    print(f'Positive Results {len(positive_results)} => {sorted(positive_results)}')
    print(f'Negative Results {len(negative_results)} => {sorted(negative_results)}')
    print('-'*200)

sad()
