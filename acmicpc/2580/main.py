max_length = 9

remain_zeros = dict()
sudoku = list()
for _ in range(max_length):
    row = [int(x) for x in input().split()]
    sudoku.append(row)


def get_base_set():
    return set(range(1,10))

def find_row(row):
    return get_base_set() - set(sudoku[row])

def find_col(col):
    return get_base_set() - set([item[col] for item in sudoku])

def find_square(row, col):
    remain_digit = get_base_set()

    square_y = (row//3)*3
    square_x = (col//3)*3
    for i in range(3):
        for j in range(3):
            digit = sudoku[square_y + i][square_x + j]
            remain_digit.discard(digit)

    return remain_digit

def find_possible_digits(zero_row, zero_col):
    row_set = find_row(zero_row)
    col_set = find_col(zero_col)
    square_set = find_square(zero_row, zero_col)
    return list(row_set & col_set & square_set)

def pop_minimum():
    minimum_coord = min(remain_zeros, key=remain_zeros.get)
    del remain_zeros[minimum_coord]
    return minimum_coord

def fill_a_zero():
    zero_row, zero_col = pop_minimum()
    possible_digits = find_possible_digits(zero_row, zero_col)

    # if all found
    if len(remain_zeros) == 0 and possible_digits:
        sudoku[zero_row][zero_col] = possible_digits[0]
        for row in sudoku:
            print(*row)
        exit(0)

    for digit in possible_digits:
        sudoku[zero_row][zero_col] = digit
        fill_a_zero()

    # if not found, recover sudoku table and zeros list
    sudoku[zero_row][zero_col] = 0
    remain_zeros[(zero_row, zero_col)] = len(find_possible_digits(zero_row, zero_col))

def append_zeros():
    for row in range(max_length):
        for col in range(max_length):
            if sudoku[row][col] == 0:
                remain_zeros[(row, col)] = len(find_possible_digits(row, col))

append_zeros()
fill_a_zero()