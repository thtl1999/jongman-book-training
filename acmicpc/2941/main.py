
convert_list = [
    'c=',
    'c-',
    'dz=',
    'd-',
    'lj',
    'nj',
    's=',
    'z='
]

def convert_and_count(input_string):
    for word in convert_list:
        while word in input_string:
            input_string = input_string.replace(word,'$',1)

    print(len(input_string))


convert_and_count(input())

