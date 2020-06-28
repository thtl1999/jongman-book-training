prime_numbers = list()

def calculate_prime_numbers(maximum):
    for n in range(2, maximum):
        is_prime = True
        for prime in prime_numbers:
            if n % prime == 0:
                is_prime = False
        if is_prime:
            prime_numbers.append(n)

def find_prime_couple(even):
    half_even = even/2

    for i in range(len(prime_numbers)):
        if prime_numbers[i] <= half_even:
            start_index = i
            break

    for i in range(start_index, len(prime_numbers)):
        if even - prime_numbers[i] in prime_numbers:
            return str(prime_numbers[i]) + ' ' + str(even - prime_numbers[i])

calculate_prime_numbers(10000)
prime_numbers.reverse()

number_of_problems = int(input())
for _ in range(number_of_problems):
    even_number = int(input())
    print(find_prime_couple(even_number))