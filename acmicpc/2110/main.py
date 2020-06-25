def find_next_house(houses, index, distance):
    for next in range(index + 1, len(houses)):
        if houses[next] - houses[index] >= distance:
            return next
    return -1

def is_distance_possible(houses, number_of_router, distance):
    previous_house_index = 0
    number_of_router -= 1

    for router in range(number_of_router):
        next = find_next_house(houses, previous_house_index, distance)
        if next == -1:
            return False
        previous_house_index = next

    return True

def binary_seach(minimum, maximum, current, upper):
    if upper:
        middle = (current + maximum)//2
        return current, middle, maximum
    else:
        middle = (minimum + current)//2
        return minimum, middle, current



houses = list()
number_of_house, number_of_router = input().split()
for _ in range(int(number_of_house)):
    houses.append(int(input()))

houses.sort()

possibles = list()
minimum = 0
maximum = ((houses[-1] - houses[0]) // (int(number_of_router) - 1)) + 1
distance = (minimum + maximum)//2

while(True):
    if distance in possibles:
        print(distance)
        break

    if is_distance_possible(houses, int(number_of_router), distance):
        upper = True
        possibles.append(distance)
    else:
        upper = False
    minimum, distance, maximum = binary_seach(minimum, maximum, distance, upper)
