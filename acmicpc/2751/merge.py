
def run_merge(left, right):
    left_index = 0
    right_index = 0
    merged_array = list()

    while left_index != len(left) or right_index != len(right):
        if left_index == len(left):
            merged_array.append(right[right_index])
            right_index += 1
            continue

        if right_index == len(right):
            merged_array.append(left[left_index])
            left_index += 1
            continue

        if left[left_index] < right[right_index]:
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1

    return merged_array

def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    return run_merge(left_array, right_array)


number_of_input = int(input())
input_array = list()

for _ in range(number_of_input):
    input_array.append(int(input()))

sorted_array = merge_sort(input_array)
for element in sorted_array:
    print(element)

# time out