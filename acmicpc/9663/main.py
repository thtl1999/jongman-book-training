N = int(input())

queen_list = list()
answer = 0

def check_row():
    if len(queen_list) == N:
        global answer
        answer += 1
        return

    unusable_pos = set()
    for i in range(len(queen_list)):
        unusable_pos.add(queen_list[i] + (len(queen_list) - i))
        unusable_pos.add(queen_list[i] - (len(queen_list) - i))
        unusable_pos.add(queen_list[i])

    usable_pos = set(range(N)) - unusable_pos

    for pos in list(usable_pos):
        queen_list.append(pos)
        check_row()
        queen_list.pop()

check_row()
print(answer)