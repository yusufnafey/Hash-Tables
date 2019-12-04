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
        return hash(key)


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
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # index = self._hash_mod(key)
        # # if index = none, save value to none index, otherwise append
        # # print(f"self storage: {self.storage[index]}")
        # if self.storage[index] is None:
        #     self.storage[index] = LinkedPair(key, value)
        # else:
        #     current_node = self.storage[index]
        #     while current_node.next:
        #         current_node = current_node.next
        #     current_node.next = LinkedPair(key, value)

        # ^ re-factored to this:
        index = self._hash_mod(key)
        current_node = self.storage[index]
        last_node = None

        while current_node and current_node.key != key:
            last_node = current_node
            current_node = last_node.next
        if current_node:
            current_node.value = value
        else:
            new_node = LinkedPair(key, value)
            new_node.next = self.storage[index]
            self.storage[index] = new_node
    ''' LECTURE
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            print(f"WARNING: Overwriting data at {index}")
        
        self.storage[index] = LinkedPair(key, value)
    '''
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if index = none, print error, otherwise set key's value to none
        if self.storage[index] is None:
            print("No key found")
        else:
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    current_node.value = None
                    print(f"Value of key {key} has been removed.")
                    return
                current_node = current_node.next
    ''' LECTURE
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print(f"WARNING: No key found")
            return

        self.storage[index] = None
    '''

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if index = none, print error, otherwise print node value
        if self.storage[index] is None:
            print("No key found")
            return None
        else:
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    print(f"Key {key} has a value of {current_node.value}")
                    return current_node.value
                current_node = current_node.next

    ''' LECTURE 
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == value:
                return self.storage[index].value
            else:
                print(f"WARNING: Key doesn't match")
                return None
        else return None
    '''

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # self.capacity *= 2
        # new_storage = [None] * self.capacity

        # for i in self.storage:
        #     new_index = self._hash_mod(i.key)
        #     new_storage[new_index] = LinkedPair(i.key, i.value)

        # self.storage = new_storage

        # new_storage = [None] * self.capacity
        # self.storage.extend(new_storage)

        for i in range(self.capacity):
            self.storage.append(None)

    ''' LECTURE
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for bucket_item in self.storage:
            new_index = self._hash_mod(bucket_item.key)
            new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)
        
        self.storage = new_storage
    '''

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

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
