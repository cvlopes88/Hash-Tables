class DynamicArray:

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        # Make sure we have open space
        if self.count >= self.capacity:
            self.double_size()
        # MAKE SURE INDEX IS IN RANGE
        if index >= self.count:
            print("ERROR: Index out of range ")
            return
        # shift everything over to right
        # Start with the last one, move it to the right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]
        # Insert our value
        self.storage[index] = value
        self.count += 1


    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        # self.capacity =
        pass



my_array = DynamicArray(4)
my_array.insert(0, 1)
my_array.insert(0, 2)
my_array.insert(1, 3)
my_array.insert(3, 4)
my_array.insert(0, 5)
my_array.append(20)

print(my_array.storage)


