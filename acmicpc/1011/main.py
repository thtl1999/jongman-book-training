
def find_max_k(distance):
    return int(distance**0.5)


def calculate_left_move(k, left_distance):
    move = 0
    while left_distance != 0:
        if k <= left_distance:
            left_distance -= k
            move += 1
        else:
            k -= 1

    return move

number_of_problems = int(input())
for _ in range(number_of_problems):
    start_point, end_point = [int(x) for x in input().split()]
    distance = end_point - start_point
    k = find_max_k(distance)
    left_distance = distance - k*k
    total_move = (k*2 - 1) + calculate_left_move(k, left_distance)
    print(total_move)
