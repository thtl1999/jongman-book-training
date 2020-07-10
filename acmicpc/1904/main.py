number_of_tiles = int(input())

answers = [0,1,2]

for i in range(number_of_tiles):
    answers.append((answers[-1] + answers[-2])%15746)

print(answers[number_of_tiles]%15746)