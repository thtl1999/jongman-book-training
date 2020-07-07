number_of_input = int(input())

coords = list()

for _ in range(number_of_input):
    coord = [int(x) for x in input().split()]
    coords.append(coord)

result = sorted(coords, key=lambda coord: (coord[0], coord[1]))

for coord in result:
    print(*coord)