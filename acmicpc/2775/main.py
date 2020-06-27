maximum = 15


floors = list()

floors.append(list(range(maximum)))

def calculate_next_floor():
    last_floor = floors[-1]
    floor = list()
    people = 0
    for house in last_floor:
        people += house
        floor.append(people)

    floors.append(floor)

for _ in range(maximum):
    calculate_next_floor()

number_of_problems = int(input())

for _ in range(number_of_problems):
    floor_number = int(input())
    house_number = int(input())
    print(floors[floor_number][house_number])