N = int(input())

array = {(i,j): True for i in range(N) for j in range(N)}
answer = 0


def unmark_array(queen_path):
    for path in queen_path:
        array[path] = False


def mark_array(queen_path):
    for path in queen_path:
        array[path] = True


def make_queen_path(row, col):
    queen_path = list()
    for k in range(1, N - row):
        left_col = col - k
        right_col = col + k
        cur_row = row + k

        # middle
        if array[(col, cur_row)]:
            queen_path.append((col, cur_row))
        # left
        if col - k >= 0 and array[(left_col, cur_row)]:
            queen_path.append((left_col, cur_row))
        # right
        if col + k < N and array[(right_col, cur_row)]:
            queen_path.append((right_col, cur_row))

    return queen_path


def set_a_queen(row):
    for col in range(N):
        if array[(col, row)]:
            if row == N - 1:
                global answer
                answer += 1
            else:
                queen_path = make_queen_path(row, col)
                unmark_array(queen_path)
                set_a_queen(row+1)
                mark_array(queen_path)

set_a_queen(0)
print(answer)