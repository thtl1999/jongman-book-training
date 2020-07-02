

six_count = 0

target_seq = int(input())

for i in range(1000000000):
    if '666' in str(i):
        six_count += 1
        if six_count == target_seq:
            print(i)
            exit()
