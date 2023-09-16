class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def peek(self):
        if self.head is None:
            raise Exception("Stack is empty")
        return self.head.data

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty")
        pop_node = self.head
        self.head = self.head.next
        pop_node.next = None
        self.size -= 1
        return pop_node.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.size


# instantiate the MyStack class
stack = MyStack()

# push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# print the top element of the stack
print(stack.peek())  # outputs: 30

# pop an element from the stack and print it
print(stack.pop())  # outputs: 30

# check if the stack is empty
print(stack.is_empty())  # outputs: False

# print the size of the stack
print(stack.size)  # outputs: 2

# print the top element of the stack
print(stack.peek())  # outputs: 20
