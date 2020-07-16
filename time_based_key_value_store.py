import collections

class TimeMap:

    def __init__(self):
        # Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. 
        # The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet).
        # Default items are created using list(), which returns a new empty list object.
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map.get(key, None)
        if not arr:
            return ""

        left = 0
        right = left(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= timestamp:
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid - 1

        return "" if right == -1 else arr[right][1] # arr[right][1] is the value stored