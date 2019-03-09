max_cal = [ 3]

multiplier = 1

try:
    if 0 == max_cal[-2]:
        multiplier = 1
        print("two skip")
    else:
        multiplier *= 3 / 2
        print("one skip")
except:
    multiplier = 1
    print("")