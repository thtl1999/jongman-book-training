a = [1,2,3,4,5,6,7,8]

b = [
    [1,2,3,4,5,6,7,8],
    [2,3,4,5,6,7,8,9],
    [3,4,5,6,7,8,9,0]
]
print('Using just print')
print(a)
print(b)

print('Using * to print')
print(*a)
for line in b:
    print(*line)