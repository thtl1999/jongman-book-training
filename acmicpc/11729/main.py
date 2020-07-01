moved = list()

def hanoi(size, cur_pos, alt_pos, target_pos):
    if size == 1:
        moved.append([cur_pos, target_pos])
        return

    # move (n-1)size circle to alt position
    hanoi(size-1, cur_pos, target_pos, alt_pos)
    # move bottom circle to target position
    moved.append([cur_pos, target_pos])
    # move (n-1)size circle in alt position to target position
    hanoi(size-1, alt_pos, cur_pos, target_pos)


number_of_circle = int(input())
hanoi(number_of_circle, 1, 2, 3)
print(len(moved))
for move in moved:
    print(*move)