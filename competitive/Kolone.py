len_r1, len_r2 = map(int, input().split())

row1 = [char for char in input()]

row2 = [char for char in input()]

second = int(input())

combined = []

for letter in row1[::-1]:
    combined.append(letter)
for letter in row2:
    combined.append(letter)

for s in range(second):
    swapped_list = []
    for i in range(len(combined)):
        if i < len(combined) - 1:
            if combined[i] in row1 and combined[i + 1] in row2 and combined[i] not in swapped_list and combined[i + 1] not in swapped_list:
                combined[i], combined[i + 1] = combined[i + 1], combined[i]
                swapped_list.append(combined[i])
                swapped_list.append(combined[i + 1])


print("".join(combined))