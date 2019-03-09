

def main():
    """
        >>>25.0 100.0
        >>>190.0 57.5
        >>>4
        >>>125.0 67.5
        >>>75.0 125.0
        >>>45.0 72.5
        >>>185.0 102.5
        19.984901
    """
    position = list(map(float, input().split()))

    goal = list(map(float, input().split()))

    canonball_count = int(input())
    canonball_list = []
    for i in range(canonball_count):
        canonball_list.append(list(map(float, input().split())))

    time = 0

    while position != goal:
        time_of_attempts = []
        new_positions = []
        speed_attempts = [[5]]
        time_of_attempts.append(distance(position, goal)/5)
        new_positions.append(goal)

        for canonball in canonball_list:
            time_of_attempts.append(distance(canonball, position)/2 + 2)

        fastest_attempt = max(speed_attempts)
        fastest_index = speed_attempts.index(fastest_attempt)

        #Execute
        time += time_of_attempts[fastest_index]
        position = new_positions[fastest_index]

    while position != goal:
        if distance(position, goal) <= 10:
            pass
        else:

    print(time)




def distance(pos1, pos2):
   return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) **.5

def fire_cannon(cannon, goal):


main()