# Implementation of Stack and Queue, Circular Queue from scratch

# Simple Stack class that allows only push and pop operations
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.stack < 1:
            return None
        else:
            return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def size(self):
        return len(self.stack)

# Simple Queue that only has enqueue and dequeue operations
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            self.queue.pop(0)

    def size(self):
        return len(self.queue)

# Circular Queue implementation
class CircularQueue:
    def __init_(self, k):
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
        self.currlen = 0
        self.maxSize = k

    # Adding elements to the queue
    def enqueue(self, data):
        if self.isFull():
            return False
        tail = (self.tail + 1) % self.maxSize
        self.queue[tail] = data
        self.tail = tail
        self.currlen += 1
        if self.currlen == 1:
            self.head = 0
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.maxSize
        self.currlen -= 1
        if self.isEmpty():
            self.head = -1
            self.tail = -1
        return True
    
    # Gets the first element from the queue
    def First(self):
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    # Gets the last element from the queue
    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    # Checks whether the circular queue is empty or not
    def isEmpty(self):
        return self.currlen == 0

    # Checks whether the circular queue is full or not
    def isFull(self):
        return self.currlen == self.maxSize