visited_table = dict()

def add_prime_numbers(prime_numbers, maximum_range):
    for n in range(2,maximum_range+1):
        is_prime = True
        for prime_number in prime_numbers:
            if n % prime_number == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(n)


def delete_prime_numbers(prime_numbers, minumum_value):
    for i in range(len(prime_numbers)):
        if prime_numbers[i] > minumum_value:
            return prime_numbers[i:]


def is_a_different(num1, num2):
    different = 0
    for n1, n2 in zip(str(num1), str(num2)):
        if n1 == n2:
            different += 1

    if different == 3:
        return True
    else:
        return False

def add_graph_element(graph, key, element):
    if key not in graph:
        graph[key] = list()
    graph[key].append(element)

def calculate_graph(prime_numbers, graph):
    for key in prime_numbers:
        for element in prime_numbers:
            if is_a_different(key, element):
                add_graph_element(graph, key, element)

# def construct_cycle_graph(cycle_graph, different_graph):
#     for key in different_graph:
#         cycle_graph[key] = dict()
#
#     for key in different_graph:
#         for element in different_graph[key]:
#             cycle_graph[key][element] = cycle_graph[element]
#
#     return cycle_graph

def find_distance(queue, graph, distance, n1, n2):
    if n1 not in visited_table:
        visited_table[n1] = distance
    elif visited_table[n1] <= distance:
        return False
    else: # visited > distance
        visited_table[n1] = distance

    if n1 == n2: # found answer
        print(distance)
        return True

    for next_prime in graph[n1]:
        queue.append([distance+1, next_prime, n2])
    return False




prime_numbers = list()
add_prime_numbers(prime_numbers, 10000)
prime_numbers = delete_prime_numbers(prime_numbers, 1000)
a_different_graph = dict()
calculate_graph(prime_numbers, a_different_graph)
# cycle_graph = dict()
# cycle_graph = construct_cycle_graph(cycle_graph, a_different_graph)

problem_length = int(input())
for _ in range(problem_length):
    n1, n2 = input().split()
    visited_table = dict()
    queue = [[0, int(n1), int(n2)]]
    while(queue):
        distance, n1, n2 = queue[0]
        found = find_distance(queue, a_different_graph, distance, n1, n2)
        if found:
            break
        queue = queue[1:]

    if not found: # could not find anything
        print('Impossible')
