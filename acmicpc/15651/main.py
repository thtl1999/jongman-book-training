maximum, length = [int(x) for x in input().split()]

range_list = list(range(1,maximum+1))

def print_permute(ongoing_list, length_left):
    for element in range_list:
        if length_left == 1:
            print(*ongoing_list, element)
        else:
            print_permute(ongoing_list + [element], length_left - 1)

print_permute([], length)