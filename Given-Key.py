from collections import defaultdict

class MyHashTable:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(list)

    def put(self, key, value):
        hash_key = hash(key) % self.size
        if not self.table[hash_key]:
            self.table[hash_key] = [(key, value)]
        else:
            for i, pair in enumerate(self.table[hash_key]):
                if pair[0] == key:
                    self.table[hash_key][i] = (key, value)
                    return
            self.table[hash_key].append((key, value))

    def contains(self, key):
        hash_key = hash(key) % self.size
        return bool(self.table[hash_key])

def test_my_hash_table():
    ht = MyHashTable()
    keys = ["one", "two", "three", "four", "five"]
    values = [1, 2, 3, 4, 5]
    for i in range(len(keys)):
        ht.put(keys[i], values[i])

    for i in range(len(keys)):
        assert ht.contains(keys[i]) == True

    assert ht.contains("unknown_key") == False

if __name__ == "__main__":
    test_my_hash_table()