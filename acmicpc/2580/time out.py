max_length = 9



def get_base_list():
    return set(range(1,10))

def find_row(sudoku_table, row):
    remain_digit = get_base_list()
    for digit in sudoku_table[row]:
        remain_digit.discard(digit)

    return remain_digit

def find_col(sudoku_table, col):
    remain_digit = get_base_list()
    for i in range(max_length):
        digit = sudoku_table[i][col]
        remain_digit.discard(digit)

    return remain_digit

def find_square(sudoku_table, row, col):
    remain_digit = get_base_list()

    square_y = (row//3)*3
    square_x = (col//3)*3
    for i in range(3):
        for j in range(3):
            digit = sudoku_table[square_y + i][square_x + j]
            remain_digit.discard(digit)

    return remain_digit

def find_zero(sudoku):
    for row in range(max_length):
        for col in range(max_length):
            if sudoku[row][col] == 0:
                return True, row, col

    return False, -1, -1

def fill_a_zero(sudoku):

    found_zero, zero_row, zero_col = find_zero(sudoku)
    if not found_zero:
        for row in sudoku:
            print(*row)
        return True

    row_set = find_row(sudoku, zero_row)
    col_set = find_col(sudoku, zero_col)
    square_set = find_square(sudoku, zero_row, zero_col)

    possible_digits = list(row_set & col_set & square_set)

    changed_row = list(sudoku[zero_row])
    for digit in possible_digits:
        changed_row[zero_col] = digit
        new_sudoku = sudoku[:zero_row] + [changed_row] + sudoku[zero_row+1:]
        if fill_a_zero(new_sudoku):
            return True


sudoku_table = list()
for _ in range(max_length):
    row = [int(x) for x in input().split()]
    sudoku_table.append(row)

fill_a_zero(sudoku_table)