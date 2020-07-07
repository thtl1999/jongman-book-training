max_length = 9

sudoku_table = list()
for _ in range(max_length):
    row = [int(x) for x in input().split()]
    sudoku_table.append(row)

def get_base_list():
    return list(range(1,10))

def find_row(row):
    remain_digit = get_base_list()
    for digit in sudoku_table[row]:
        if digit in remain_digit:
            remain_digit.remove(digit)

    return remain_digit

def find_col(col):
    remain_digit = get_base_list()
    for i in range(max_length):
        digit = sudoku_table[i][col]
        if digit in remain_digit:
            remain_digit.remove(digit)

    return remain_digit

def find_square(row, col):
    remain_digit = get_base_list()

    square_y = (row//3)*3
    square_x = (col//3)*3
    for i in range(3):
        for j in range(3):
            digit = sudoku_table[square_y + i][square_x + j]
            if digit in remain_digit:
                remain_digit.remove(digit)

    return remain_digit

def try_fill(row, col):
    row_set = set(find_row(row))
    col_set = set(find_col(col))
    square_set = set(find_square(row, col))

    remain_digit = row_set & col_set & square_set

    if len(remain_digit) == 1:
        sudoku_table[row][col] = remain_digit.pop()


is_processing = True
while is_processing:
    is_processing = False
    for row in range(max_length):
        for col in range(max_length):
            if sudoku_table[row][col] == 0:
                is_processing = True
                try_fill(row,col)

for row in sudoku_table:
    print(*row)