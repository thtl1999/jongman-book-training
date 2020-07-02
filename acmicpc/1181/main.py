
words = list()
for _ in range(int(input())):
    word = input()
    if word not in words:
        words.append(word)

maximum_length = 55
sorted = [list() for _ in range(maximum_length)]
for word in words:
    sorted[len(word)].append(word)

for length_sorted in sorted:
    length_sorted.sort()
    for word in length_sorted:
        print(word)
