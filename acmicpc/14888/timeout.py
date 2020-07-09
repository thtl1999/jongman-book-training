from itertools import permutations

def my_add(front, rear):
    return front + rear

def my_sub(front, rear):
    return front - rear

def my_mul(front, rear):
    return front * rear

def my_div(front, rear):
    if front < 0:
        return -(abs(front)//rear)
    else:
        return front//rear


number_of_input = int(input())
numbers = [int(x) for x in input().split()]
operator_counts = [int(x) for x in input().split()]

operators = list()
operator_list = ['+','-','*','/']
for i in range(4):
    operator = operator_list[i]
    for _ in range(operator_counts[i]):
        operators.append(operator)

permutes = set(permutations(operators))
results = list()

# for p in permutes:
#     print(p)

func_dict = {
    '+': my_add,
    '-': my_sub,
    '*': my_mul,
    '/': my_div
}

memo = dict()

def calculate(front, remain_operators, start_index):
    remain_numbers = numbers[len(numbers) - len(remain_operators):]
    result = front
    for i, operator in enumerate(remain_operators):
        result = func_dict[operator](result,remain_numbers[i])
        memo[remain_operators[:i+1]] = result

    return result

for operator_combo in permutes:
    front = numbers[0]
    found = False
    for i in range(1, len(operator_combo)):
        if operator_combo[:-i] in memo:
            found = True
            front = memo[operator_combo[:-i]]
            result = calculate(front, operator_combo, len(operator_combo) - i)
            break

    if not found:
        result = calculate(front, operator_combo, 0)

    results.append(result)

print(max(results))
print(min(results))