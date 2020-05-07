class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

    # def fnv1(self, key):
    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)

        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):

        index = self.hash_index(key)
        current_node = self.storage[index]

        if not current_node:
            self.storage[index] = HashTableEntry(key, value)
            return

        while current_node:
            if current_node.key == key:
                current_node.value = value
                return
            elif not current_node.next:
                current_node.next = HashTableEntry(key, value)
                return
            else:
                current_node = current_node.next

    def delete(self, key):

        index = self.hash_index(key)
        current_node = self.storage[index]

        if current_node.key == key:
            self.storage[index] = current_node.next
            current_node.next = None
            return

        while current_node.next:
            if current_node.next.key == key:
                delete_node = current_node.next
                current_node.next = delete_node.next
                delete_node.next = None
                return
            else:
                current_node = current_node.next
        return print('Warning: Key is not found')

    def get(self, key):

        index = self.hash_index(key)
        current_node = self.storage[index]

        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next

        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
