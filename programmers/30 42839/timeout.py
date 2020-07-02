def find_prime(maximum):
    primes = list()
    for i in range(2, maximum+1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes

def solution(numbers_string):
    numbers = [s for s in numbers_string]
    numbers.sort()
    numbers.reverse()
    maximum = int(''.join(numbers))
    primes = find_prime(maximum)

    prime_count = 0
    for prime in primes:
        prime_splited = [n for n in str(prime)]
        temp_numbers = list(numbers)
        has_all_digit = True
        for digit in prime_splited:
            if digit in temp_numbers:
                temp_numbers.remove(digit)
            else:
                has_all_digit = False
        if has_all_digit:
            prime_count += 1

    return prime_count