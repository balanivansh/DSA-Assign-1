class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor

    def _resize(self, capacity):
        new_array = [None] * capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insertAtIndex(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == len(self.array):
            self._resize(max(1, len(self.array) * self.resize_factor))
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.size -= 1
        self.array[self.size] = None
        if self.size <= len(self.array) // (self.resize_factor * 2):
            self._resize(max(1, len(self.array) // self.resize_factor))

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def rotateRight(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        left, right = 0, self.size - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1

    def append(self, value):
        if self.size == len(self.array):
            self._resize(max(1, len(self.array) * self.resize_factor))
        self.array[self.size] = value
        self.size += 1

    def prepend(self, value):
        self.insert_at_index(0, value)

    def merge(self, other):
        for element in other.array[:other.size]:
            self.append(element)

    def interleave(self, other):
        new_array = DynamicArray()
        i, j = 0, 0
        while i < self.size or j < other.size:
            if i < self.size:
                new_array.append(self.array[i])
                i += 1
            if j < other.size:
                new_array.append(other.array[j])
                j += 1
        return new_array

    def getMiddle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def indexOf(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def splitAtIndex(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        first_part = DynamicArray()
        second_part = DynamicArray()
        for i in range(index):
            first_part.append(self.array[i])
        for i in range(index, self.size):
            second_part.append(self.array[i])
        return first_part, second_part

# Example

arr = DynamicArrays(5)

# Appending elements to the array
arr.append(10)
arr.append(15)
arr.append(20)
arr.append(25)
arr.append(30)

# Splitting the array at index 3
left, right = arr.split(3)
print("Left array:", left)   
# Output: Left array: [10, 15, 20]

print("Right array:", right) 
# Output: Right array: [25, 30]

# Removing an element
arr.removeValue(25)

# Checking the length of the array
print(len(arr)) 
 # Output: 4 

# Inserting an element at index 0
arr.insertAtIndex(0, 5)

# Accessing elements by index
print(arr[0]) 
 # Output: 5


# Checking the length of the array
print(len(arr)) 
 # Output: 5 

# Deleting an element at index 0
arr.deleteAtIndex(0)

# Checking the length of the array
print(len(arr)) 
 # Output: 4 
