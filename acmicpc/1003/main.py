number_of_input = int(input())
memo = dict()

def fibo_count(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1, 0
    if n == 1:
        return 0, 1

    zero1, one1 = fibo_count(n-1)
    zero2, one2 = fibo_count(n-2)

    memo[n] = (zero1 + zero2, one1 + one2)

    return memo[n]

for _ in range(number_of_input):
    zero, one = fibo_count(int(input()))
    print(zero, one)