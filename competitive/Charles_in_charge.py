city_count, highway_count, percentage = map(int, input().split())

highways = []

for i in range(highway_count):
    highways.append(list(map(int, input().split())))
for highway in highways:
    if highway[0] == 1 and highway[1] == city_count:
        max_distance = (highway[2] * (percentage + 100)) // 100

min_route_bool = False
min_route = max_distance

while min_route_bool != True:
    current_position = 1
    for highway in highways:
        if highway[0] == current_position and highway[2] < min_route:
            min_route = highway[2]
            print(min_route)





print(city_count)
print(highway_count)
print(percentage)
print(highways)