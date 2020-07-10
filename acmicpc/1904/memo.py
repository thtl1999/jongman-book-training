number_of_tiles = int(input())

memo = dict()


def put_tile(space_left):
    if space_left in memo:
        return memo[space_left]

    if space_left < 3:
        return space_left

    memo[space_left] = put_tile(space_left - 2) + put_tile(space_left - 1)
    return memo[space_left]


print(put_tile(number_of_tiles))