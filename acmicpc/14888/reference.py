number_of_input = int(input())

numbers = [int(x) for x in input().split()]

a, s, m, d = [int(x) for x in input().split()]

results = list()

def calculate(index, a,s,m,d, value):
    if index == len(numbers):
        results.append(value)
        return

    if a > 0:
        calculate(index + 1, a - 1, s, m, d, value + numbers[index])
    if s > 0:
        calculate(index + 1, a, s - 1, m, d, value - numbers[index])
    if m > 0:
        calculate(index + 1, a, s, m - 1, d, value * numbers[index])
    if d > 0:
        calculate(index + 1, a, s, m, d - 1, int(value/numbers[index]))

calculate(1, a,s,m,d, numbers[0])
print(max(results))
print(min(results))