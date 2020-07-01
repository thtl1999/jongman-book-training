memo = dict()

def fibo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

print(fibo(int(input())))