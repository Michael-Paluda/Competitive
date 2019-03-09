n = int(input())

for i in range(n):

    count = 0

    digits = input().split()

    if len(digits[1]) != len(digits[0]):

        adding_length = len(digits[1]) - len(digits[0])

        digits[0] = "0"*adding_length + digits[0]


    digit1 = [int(char) for char in digits[0]]
    digit2 = [int(char) for char in digits[1]]



    while digit1 != digit2:
        count += sum(digit1)
        '''if digit1[-1] == 9:
            digit1[-1] = 0
            digit1[-2] += 1
        else:
            digit1[-1] += 1
        '''
        for i in range(len(digit1) - 1,-1, -1):
            if digit1 == digit2:
                break
            elif digit1[i] != 9:
                digit1[i] += 1
                break
            else:
                digit1[i] = 0




    count += sum(digit2)

    print(count)