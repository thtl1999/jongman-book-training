class Gear:
    def __init__(self, polarity, prev_gear, score):
        self.polarity = polarity
        self.center = 0
        self.prev = prev_gear
        self.next = None
        self.score = score

        if prev_gear:
            prev_gear.next = self

    def rotate_left(self, check_direction):
        if (check_direction == 'both' or check_direction == 'prev') and self.prev:
            if self.prev.get_right_value() != self.get_left_value():
                self.prev.rotate_right('prev')

        if (check_direction == 'both' or check_direction == 'next') and self.next:
            if self.next.get_left_value() != self.get_right_value():
                self.next.rotate_right('next')

        self.center = (self.center + 1) % len(self.polarity)

    def rotate_right(self, check_direction):
        if (check_direction == 'both' or check_direction == 'prev') and self.prev:
            if self.prev.get_right_value() != self.get_left_value():
                self.prev.rotate_left('prev')

        if (check_direction == 'both' or check_direction == 'next') and self.next:
            if self.next.get_left_value() != self.get_right_value():
                self.next.rotate_left('next')

        self.center = (self.center - 1) % len(self.polarity)

    def get_right_value(self):
        right = (self.center + 2) % len(self.polarity)
        return self.polarity[right]

    def get_left_value(self):
        left = (self.center - 2) % len(self.polarity)
        return self.polarity[left]

    def get_score(self):
        if self.polarity[self.center] == '1':
            return self.score
        else:
            return 0


prev_gear = None
gears = list()
for score in [1,2,4,8]:
    polarity = [ns for ns in input()]
    gear = Gear(polarity, prev_gear, score)
    prev_gear = gear
    gears.append(gear)

number_of_rotation = int(input())
for _ in range(number_of_rotation):
    gear_number, direction = input().split()
    gear = gears[int(gear_number) - 1]
    if direction == '1':
        gear.rotate_right('both')
    else:
        gear.rotate_left('both')

result = 0
for gear in gears:
    result += gear.get_score()

print(result)