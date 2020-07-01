
list_size = 3

correct_list = [['*' for _ in range(list_size)] for _ in range(list_size)]

incorrect_list = [['*']*list_size]*list_size

print('These list looks same...')
print('Good', correct_list)
print('Bad!', incorrect_list)

print('Change 2nd list value')
correct_list[1][1] = ' '
incorrect_list[1][1] = ' '
print('Good', correct_list)
print('Bad!', incorrect_list)

print('ID of internal list of correct list')
for l in correct_list:
    print(id(l))

print('ID of internal list of incorrect list')
for l in incorrect_list:
    print(id(l))
    