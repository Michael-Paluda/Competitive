import os

def longest_palindrome(input):
    longest = ''
    for i in range(len(input)):
        for j in range(0, i):
            new = input[j:i + 1]
            no_space = new.replace(' ','')
            if no_space == no_space[::-1] and len(new) > len(longest):
                longest = new
    if len(longest)<2:
        return ''
    else:
        return longest




if __name__ == "__main__":

    try:
        input = str(input())
    except:
        input = None

    res = longest_palindrome(input)
    print(res + "\n")



