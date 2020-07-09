from itertools import combinations

number_of_people = int(input())

power_table = list()
for person in range(number_of_people):
    person_power = [int(x) for x in input().split()]
    power_table.append(person_power)

def get_score(team):
    team_members = list(team)
    team_combos = combinations(team_members, 2)
    score = 0
    for team_combo in team_combos:
        score += power_table[team_combo[0]][team_combo[1]]
        score += power_table[team_combo[1]][team_combo[0]]
    return score

combos = combinations(list(range(number_of_people)), number_of_people//2)
results = list()
for combo in combos:
    team = set(combo)
    opponent = set(range(number_of_people)) - team
    results.append(abs(get_score(team) - get_score(opponent)))

print(min(results))