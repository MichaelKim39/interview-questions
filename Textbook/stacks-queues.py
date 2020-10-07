class Node:
    def __init__(self, data=None):
        super(self)
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        topData = self.top.data
        self.top = top.next
        return topData

    def push(self):
        temp = Node(None)
        temp.next = top
        top = temp

    def peek(self):
        return self.top.data

    def isEmpty(self):
        return top == None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        temp = Node(data)
        if self.last is not None:
            self.last.next = temp
        self.last = temp
        if self.first is None:
            self.first = self.last

    def dequeue(self):
        data = self.first.data
        if self.first is None:
            self.last = None
        self.first = self.first.next
        return data

    def peek(self):
        return self.first.data

    def isEmpty(self):
        return self.first is None


class MinStack(Stack):
    def __init__(self):
        super().__init__(self)
        self.minStack = Stack(Node(None))

    def push(self, value):
        if value <= min():
            self.minStack.push(value)
        super.push(self, value)

    def pop(self, value):
        value = super.pop(self)
        if value == min():
            self.minStack.pop()
        return value

    def min(self):
        if self.minStack.isEmpty():
            return float("inf")
        else:
            return self.minStack.peek()
