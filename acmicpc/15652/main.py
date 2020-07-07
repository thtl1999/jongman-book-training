maximum, length = [int(x) for x in input().split()]

range_list = list(range(1,maximum+1))

def print_permute(ongoing_list, length_left):
    if length_left == 0:
        print(*ongoing_list)
        return

    for element in range_list[ongoing_list[-1] - 1:]:
        if length_left == 1:
            print(*ongoing_list, element)
        else:
            print_permute(ongoing_list + [element], length_left - 1)


for element in range_list:
    print_permute([element], length - 1)