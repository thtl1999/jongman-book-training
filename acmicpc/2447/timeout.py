basic_table = [['*']]
pattern = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]


def broaden_table():
    new_table = list()
    for row in range(len(basic_table)*3):
        new_table.append(list())

    for i, row in enumerate(pattern):
        for j, col in enumerate(row):
            for k, line in enumerate(basic_table):
                for char in line:
                    if col and char == '*':
                        new_table[i*len(basic_table) + k].append('*')
                    else:
                        new_table[i*len(basic_table) + k].append(' ')

    return new_table


def print_table():
    for line in basic_table:
        print(''.join(line))


number_of_iteration = int(int(input())**(1/3))

for _ in range(number_of_iteration):
    basic_table = broaden_table()

print_table()