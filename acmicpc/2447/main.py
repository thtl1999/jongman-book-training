

array_size = int(input())

array = [[' ' for _ in range(array_size)] for _ in range(array_size)]

def draw_star(x,y):
    for i in range(3):
        for j in range(3):
            array[x+i][y+j] = '*'
    array[x+1][y+1] = ' '

def recursive(x, y, size):
    if size == 3:
        draw_star(x,y)
        return

    split_size = int(size / 3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            recursive(x + i*split_size, y + j*split_size, split_size)

recursive(0, 0, array_size)

for line in array:
    print(*line, sep='')