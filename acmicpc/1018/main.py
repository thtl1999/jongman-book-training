

n_of_rows, n_of_cols = [int(x) for x in input().split()]

table = list()

for _ in range(n_of_rows):
    table.append(input())

default_size = 8
minimum = default_size * default_size

def reverse_color(color):
    if color == 'W':
        return 'B'
    else:
        return 'W'

def find_minimum_change(start_x, start_y):
    change_count = 0
    color = 'W'
    for x in range(default_size):
        color = reverse_color(color)
        for y in range(default_size):
            if color != table[start_y + y][start_x + x]:
                change_count += 1
            color = reverse_color(color)

    return min(change_count, default_size*default_size - change_count)

for start_x in range(n_of_cols - default_size + 1):
    for start_y in range(n_of_rows - default_size + 1):
        value = find_minimum_change(start_x, start_y)
        if value < minimum:
            minimum = value

print(minimum)