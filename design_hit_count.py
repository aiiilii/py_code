class HitCounter:

    # The third solution creates an array of 300 elements. Every element of the array comprises of [frequency, timestamp].
    # Timestamp 1 maps to index 0. Timestamp 100 maps to index 99.
    # Use modulo mathematics to update it. hit: O(1). get_hit: O(300). 
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = [[0, i + 1] for i in range(300)]
        return
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # ts = 301 means (301-1)%300
        idx = int((timestamp - 1) % 300)
        if self.counter[idx][1] == timestamp:
            self.counter[idx][0] += 1
        else:
            self.counter[idx][0] = 1
            self.counter[idx][1] = timestamp
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        for x in self.counter:
            c, t = x[0], x[1]
            if timestamp - t < 300:
                count += c
        return count