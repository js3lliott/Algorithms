class DynamicArray:

    def __init__(self):
        self.array = [0] * 2
        self.currentIndex = 0
        self.capacity = 2

    def add(self, item):
        if (self.currentIndex == self.capacity):
            self.resizeArray()
        self.array[self.currentIndex] = item
        self.currentIndex += 1

    def remove(self):
        if (self.currentIndex == 0):
            raise Exception ("Cannot remove from empty list")
        self.currentIndex -= 1

    def resizeArray(self):
        self.capacity *= 2 
        newArr = [0] * self.capacity
        for i in range(len(self.array)):
            newArr[i] = self.array[i]
        self.array = newArr

    def get(self, index):
        if (index < 0 or index >= self.currentIndex):
            raise Exception ("Index out of range")
        return self.array[index]

    def size(self):
        return len(self.array)


arr = DynamicArray()
arr.add(12)       # [12]
arr.add(31)       # [12, 31]
arr.add(6)        # [12, 31, 6]
print(arr.size()) # 3
print(arr.get(2)) # 31
arr.remove()      # [12, 31]
print(arr.size()) # 2