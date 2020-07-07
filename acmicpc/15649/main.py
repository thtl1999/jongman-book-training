from itertools import permutations


maximum, length = [int(x) for x in input().split()]

permutation_list = list(permutations(list(range(1, maximum+1)), length))

for permute in permutation_list:
    print(*permute)