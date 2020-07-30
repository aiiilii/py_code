from typing import List
import collections

class MostCommonWord:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Replace the punctuations with spaces,
        # and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

        words = normalized_str.split()

        word_count = collections.defaultdict(int)
        banned_words = set(banned)

        for word in words:
            if word not in banned_words:
                word_count[word] += 1

        # Return the word with the highest frequency
        return max(word_count.items(), key = operator.itemgetter(1))[0]