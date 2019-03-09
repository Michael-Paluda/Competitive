
correct = int(input())

answers = [x for x in input()]

friend = [x for x in input()]

questions = len(answers)

same = 0



for i in range(questions):
    if answers[i] == friend[i]:
        same += 1

incorrect = 0


incorrect += abs(same - correct)


print(questions - incorrect)


