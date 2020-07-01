array_size = int(input())

array = list()

for _ in range(array_size):
    array.append(input())

def check_identical(x, y, size):
    value = array[y][x]
    for i in range(size):
        for j in range(size):
            if array[y+i][x+j] != value:
                return zip(x, y, size)

    return value

def zip(x, y, size):
    if size == 1:
        return array[y][x]

    result = '('

    new_size = int(size/2)

    for i, j in [[0,0],[1,0],[0,1],[1,1]]:
        result += check_identical(x+i*new_size, y+j*new_size, new_size)

    result += ')'
    return result

print(check_identical(0, 0, array_size))