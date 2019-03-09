




N = int(input())

for i in range(N):
    rope_length = 0
    knot_rope = []
    rope_count = int(input())

    bag = [(int(i[:-1]), i[-1]) for i in input().split()]

    bag.sort(key=lambda tup: tup[0], reverse=True)

    knot_rope.append(bag[0])
    del bag[0]

    blues = []
    reds = []

    for rope in bag:
        if rope[1] =="B":
            blues.append(rope)
        else:
            reds.append(rope)

    for rope in knot_rope:
        if rope[1] == "B":
            try:
                knot_rope.append(reds[0])
                del reds[0]
            except:
                break
        else:
            try:
                knot_rope.append(blues[0])
                del blues[0]
            except:
                break

    if knot_rope[-1][1] == knot_rope[0][1]:
        del knot_rope[-1]

    if len(knot_rope) < 2:
        rope_length = 0
    else:
        for rope in knot_rope:
            rope_length += rope[0]

        rope_length -= len(knot_rope)


    print("Case #{0}: {1}".format(i + 1, rope_length))














