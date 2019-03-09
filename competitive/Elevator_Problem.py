import time

def calculate_elevator_path(floors, pos, goal, up, down):
    t0 = time.time()
    moves = 0
    impossible = False
    while pos != goal:
        t1 = time.time()
        if t1 - t0 > .8:
            return 'use the stairs'
        if impossible == True:
            return 'use the stairs'

        if pos > goal and down != 0:

            while pos - down < 1:
                impossible = True
                pos += up
                moves += 1

            pos -= down
            moves += 1

        elif pos < goal and up != 0:

            while pos + up > floors:
                impossible = True
                pos -= down
                moves += 1
            pos += up
            moves += 1
        else:
            return 'use the stairs'


    return moves

floors, start, goal, up, down, = map(int, input().split())

print(calculate_elevator_path(floors, start, goal, up, down))

