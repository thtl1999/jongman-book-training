class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None

    def get_size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return 1
        else:
            return 0

    def get_front(self):
        if self.front:
            return self.front.get_value()
        else:
            return -1

    def get_back(self):
        if self.back:
            return self.back.get_value()
        else:
            return -1

    def pop(self):
        if self.size == 0:
            return -1
        else:
            self.size = self.size - 1

            front = self.front
            self.front = front.get_next()

            if self.size == 0:
                self.back = None

            return front.get_value()

    def push(self, value):
        self.size = self.size + 1
        new_item = Queue_item(value)
        if self.size == 1:
            self.front = new_item
        else:
            self.back.set_next(new_item)
        self.back = new_item

class Queue_item:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next
    
    
def get_command():
    input_array = input().split(' ')
    if len(input_array) == 1:
        return input_array[0], None
    else:
        return input_array[0], input_array[1]


# main
queue = Queue()
number_of_commands = int(input())

command_map = {
    'push': queue.push,
    'pop': queue.pop,
    'size': queue.get_size,
    'empty': queue.is_empty,
    'front': queue.get_front,
    'back': queue.get_back
}

for _ in range(number_of_commands):
    command, argument = get_command()
    if command == 'push':
        command_map[command](argument)
    else:
        return_value = command_map[command]()
        if return_value is not None:
            print(return_value)