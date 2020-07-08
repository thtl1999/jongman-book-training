N = int(input())

array = {(i,j): 0 for i in range(N) for j in range(N)}
answer = 0


def mark_array(row, col, sign):
    for k in range(1, N - row):
        # middle
        array[(col, row + k)] += sign
        # left
        if col - k >= 0:
            array[(col - k, row + k)] += sign
        # right
        if col + k < N:
            array[(col + k, row + k)] += sign


def set_a_queen(row):
    if row == N:
        global answer
        answer += 1
        return

    for col in range(N):
        if array[(col, row)] == 0:
            mark_array(row, col, 1)
            set_a_queen(row+1)
            mark_array(row, col, -1)

set_a_queen(0)
print(answer)