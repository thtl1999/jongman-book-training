number_of_house = int(input())

house_costs = list()

for _ in range(number_of_house):
    house_costs.append([int(x) for x in input().split()])

cost_sums = [list(house_costs[0])]

for house in range(1, number_of_house):
    house_cost = house_costs[house]
    last_sum = cost_sums[-1]
    r = min(last_sum[1],last_sum[2]) + house_cost[0]
    g = min(last_sum[0],last_sum[2]) + house_cost[1]
    b = min(last_sum[0],last_sum[1]) + house_cost[2]

    cost_sums.append([r,g,b])

print(min(cost_sums[-1][i] for i in range(3)))