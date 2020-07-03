import sys

def input():
    return sys.stdin.readline()

def print(sth):
    sys.stdout.write(str(sth)+'\n')

maximum_value = 1000000

number_of_input = int(input())

radix_list = [False for _ in range(maximum_value*2 + 1)]

for n in range(number_of_input):
    value = int(input())
    radix_list[value + maximum_value]  = True

for radix in range(len(radix_list)):
    if radix_list[radix]:
        print(radix - maximum_value)
