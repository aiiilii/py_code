from typing import List
import collections
import heapq

class TopKFrequent:

    # using dictionay - O(n log n)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
        res = sorted(dict, key = lambda x: (-dict[x], x))
        return res[:k]

    
    # using heap - O(n + n log k)
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words) # put the words and the corresponding counts of that word in to a dictionary : {'word1': 1, 'word2': 3}
        heap = []

        for key, val in count.items(): # key is the word, val is the count
            heapq.heappush(heap, Word(val, key)) # default is min heap
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word # max heap
        return self.freq < other.freq # min heap

    # not needed
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word