class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.next = {}
        self.before = {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.before[b] = b, a

    def delete(self, key):
        self.connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key] # delete the before pointer to key and next pointer to key by deleting the key-value pair in before dict and next dict;

    def append(self, key, val):
        self.cache[key] = val
        self.connect(self.before[self.tail], key) # append to the end
        self.connect(key, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head]) # delete the lru at the front

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache[key] 
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(key)

        self.append(key, value)
