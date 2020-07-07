from itertools import combinations

maximum, length = [int(x) for x in input().split()]

combination_range = list(range(1,maximum+1))
combination_list = list(combinations(combination_range, length))

for comb in combination_list:
    print(*comb)