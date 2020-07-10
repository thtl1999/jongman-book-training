number_of_tiles = int(input())

def put_tile(space_left):
    if space_left < 3:
        return space_left

    return put_tile(space_left - 2) + put_tile(space_left - 1)

print(put_tile(number_of_tiles))