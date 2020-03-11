import hashlib
# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity



    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hashlib.sha256(key.encode())


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):

        index = self._hash_mod(key)
        # create a new linked list node using key and value
        new_node = LinkedPair(key, value)

        # traverse the linked list in storage at generated index
        cur = self.storage[index]
        # if no list exists, new node becomes the head
        if cur is None:
            self.storage[index] = new_node
            return
        prev = None
        while cur is not None:
            # if key in list matches given key, overwrite value
            if cur.key == key:
                cur.value = value
                return
            prev = cur
            cur = cur.next
        # if reach end of list, add new node
        prev.next = new_node
        self.size += 1
        # find load factor
        lf = self.size / self.capacity
        # if load factor is greater than 0.7, resize hash table
        if lf > 0.7:
            self.resize(2)
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
         # calculate the key with the hash
         # if count < capacity
         # if value at that index is None
        '''




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            self.storage[index] = None
        else:
            print("Key not Found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # index = self._hash(key)
        # if self.storage[index] is None:
        #     print("ERROR: that key dont exist")
        # else:
        #     # loop through and see if u find the value
        #     for i in self.storage[index]:
        #         if i[0] == key:
        #             return i[1]
        index = self._hash_mod(key)

        return self.storage[index]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        # store reference to old storage
        # double the capacity by multiplying self.capacity by 2
        # reassign self.storage to [None] * capacity
        # self.capacity *= 2
        # new_storage = [None] * self.capacity
        # for i in range(self.count):
        #     new_storage[i] = self.storage[i]
        # self.storage = new_storage
        old_storage = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for bucket_item in old_storage:
            self.insert(bucket_item)


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizingg
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
