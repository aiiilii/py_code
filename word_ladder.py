from typing import List
import string

class WordLadder:

    # Time Complexity O(n*26^wordLength)
    # Space Complexity O(n)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0

        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        alpha = string.ascii_lowercase

        begin = set()
        end = set()

        begin.add(beginWord)
        end.add(endWord)
        wordList.discard(beginWord)
        wordList.discard(endWord)

        step = 2

        while begin:
            temp = set()
            for word in begin:
                for i in range(len(word)):
                    for ch in alpha:
                        new_word = word[:i] + ch + word[i + 1:]
                        if new_word in end:
                            return step
                        if new_word in wordList:
                            temp.add(new_word)
                            wordList.discard(new_word)
            step += 1
            if len(temp) <= len(end):
                begin = temp
            else:
                begin = end
                end = temp

        return 0
