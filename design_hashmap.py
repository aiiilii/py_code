class ListNode:
    def __init__(self, key=0, val=0, next=None):
        self.pair = (key, val) # create a tuple
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 2069
        self.hash = [None] * self.m


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = self.getIndex(key)
        if not self.hash[index]:
            self.hash[index] = ListNode(key, value)
        else:
            curr = self.hash[index]
            while True: # will at least execute once until reaches break when curr.next == None
                if curr.pair[0] == key:
                    curr.pair = (key, value) # update the tuple by reassigning the entire tuple
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = ListNode(key, value) # putting the new node at the end of the list

    
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = self.getIndex(key)
        curr = self.hash[index]
        while curr:
            if curr.pair[0] == key:
                return curr.pair[1]
            curr = curr.next
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = self.getIndex(key)
        curr = prev = self.hash[index]
        if not curr:
            return

        if curr.pair[0] == key:
            self.hash[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.pair[0] == key:
                    prev.next = curr.next # skip curr by connecting prev and curr.next together
                    break
                curr = curr.next
                prev = prev.next


    def getIndex(self, key: int) -> int:
        return key % self.m