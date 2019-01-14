class HashTable:
    """Hash Table Class"""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = [None] * size

    def __repr__(self):
        return(f'Graph: {self.table_size}')

    def __str__(self):
        return f'{self.table_size}'

    def _hash_key(self, key):
        """Function to create a hash from a given key."""
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Function to add a key and value into the hash table."""
        key_hash = self._hash_key(key)
        key_value = [key, value]

        if self.hashtable[key_hash] is None:
            self.hashtable[key_hash] = list([key_value])
            return True
        else:
            for pair in self.hashtable[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hashtable[key_hash].append(key_value)
            return True

    def get(self, key):
        """Function to retrieve a value from the hash table by key."""
        key_hash = self._hash_key(key)
        if self.hashtable[key_hash] is not None:
            for pair in self.hashtable[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return('The value is not in the table')

    def remove(self, key):
        """Function to retrieve and remove a value from the hash table by key."""
        key_hash = self._hash_key(key)
        if self.hashtable[key_hash] is None:
            return('False')
        for i in range(0, len(self.hashtable[key_hash])):
            if self.hashtable[key_hash][i][0] == key:
                self.hashtable[key_hash].pop(i)
                return('True')

    def state_contents(self):
        for item in self.hashtable:
            if item is not None:
                print(item)
