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
    def __init__(self, k):
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


# # Breadth First Search using Queue - rough pseudocode
# # Template 1
# def BFS(root, target):
#     queue = [] # store all nodes which are waiting to be processed
#     step = 0 # number of steps needed from root to current node

#     # initialize
#     add root to queue

#     # BFS
#     while queue is not empty:
#         step += 1
#         # iterate through the nodes which are already in the queue
#         size = len(queue)
#         for i in range(size):
#             curr = first node in queue
#             return step if curr is target
#             for next -> neighbors of curr:
#                 add next to queue

#             remove the first node in the queue

#     return -1

# # Template 2 - BFS and Queue
# def BFS(root, target):
#     queue = [] # store all nodes which are waiting to be processed
#     visited = {} # store all nodes that we've visited
#     step = 0 # number of steps needed from root to the current node

#     add root to queue
#     add root to visited

#     while queue is not empty:
#         step += 1
#         # iterate the nodes which are already in the queue
#         size = len(queue)
#         for i in range(size):
#             curr = first node in the queue
#             return step if curr is target
#             for next -> neighbors of curr:
#                 if next is not in visited:
#                     add next to queue
#                     add next to visited
#                 remove the first node from the queue
#     return -1