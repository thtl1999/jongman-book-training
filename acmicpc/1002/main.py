import math

def check_circle_overlap(distance, r1, r2):
    # if two circle has same center
    if distance == 0:
        if r1 == r2:
            return -1
        else:
            return 0

    # two circle meet in one point
    if math.isclose(distance, r1 + r2):    # distance == r1 + r2
        return 1

    # two circle are too far
    if distance > r1 + r2:
        return 0

    # two circle meets in 2 points
    if distance > r1:
        return 2

    # circle 2 is inside in circle 1
    if math.isclose(distance + r2, r1):
        return 1

    if distance + r2 > r1:
        return 2

    if distance + r2 < r1:
        return 0




    print('Not expected situation')
    return None

number_of_problems = int(input())

for _ in range(number_of_problems):
    x1, y1, r1, x2, y2, r2 = list(map(float, input().split()))
    # set circle 1 is always bigger
    if r2 > r1:
        x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

    distance_between_people = ((x1-x2)**2 + (y1-y2)**2)**0.5

    print(check_circle_overlap(distance_between_people, r1, r2))