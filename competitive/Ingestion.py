import math
multiplier = 1
n, m = map(int, input().split())

courses = list(map(int, input().split()))


max_cal = []
temp_m = m

for i in range(0, len(courses)):
    temp_m = math.floor(m * multiplier)
    eat = 0
    skip = 0
    two_skip = 0

    eat_multiplier = multiplier
    for j in range(i, len(courses)):
        eat += math.floor(min(courses[j], m * eat_multiplier))
        eat_multiplier *= 2 / 3

    if temp_m < m:
        skip_multiplier = multiplier * 3/2
    else:
        skip_multiplier = multiplier
    for j in range(i + 1, len(courses)):
        skip += math.floor(min(courses[j], m * skip_multiplier))

        skip_multiplier *= 2/3

    two_multiplier = 1
    for j in range(i + 2, len(courses)):
        two_skip += math.floor(min(courses[j], m * two_multiplier))
        two_multiplier *= 2/3

    if eat >= skip and eat >= two_skip:
        max_cal.append(min(courses[i], temp_m))
        multiplier *= 2/3

    else:
        max_cal.append(0)

        try:
            if 0 == max_cal[-2]:
                multiplier = 1
            else:
                multiplier *= 3/2
        except:
            multiplier = 1

print(sum(max_cal))