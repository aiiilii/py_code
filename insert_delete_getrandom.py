import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here
        """
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False

        # save val in dict as the length of the list before inserting into the list, this acts as index
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_element = self.list[-1]
            index = self.dict[val]
            self.list[index] = last_element # override the value of the index at val with the last_element
            self.dict[last_element] = index # change the last_element's index to val's index
            self.list.pop() # pop out the last element
            del self.dict[val] # delete the val from the dictionary
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)