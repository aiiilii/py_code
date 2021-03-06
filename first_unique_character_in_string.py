import collections

class FirstUniqueCharacter:

    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1: # if c ocurred only once in count
                return i
        return -1