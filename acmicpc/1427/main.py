not_sorted = input()

digits = [str(n) for n in range(10)]
digits.reverse()
result = ''

for digit in digits:
    for n in not_sorted:
        if n == digit:
            result += n

print(result)