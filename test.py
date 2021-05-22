def sad():

    for inp_number in range(0, 21):

        number = [int(i) for i in str(inp_number)]

        check = 0
        counter = 0

        while check != 1:

            counter += 1

            check = (number[0] ** 2)
            print(f'[1] Checking {inp_number} > {number[0]}² = {check}')


sad()