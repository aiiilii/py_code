from typing import List
import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.the_word = ""

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.root
        for w in word:
            temp = temp.children[w] # need to use bracket here because assigning
        temp.the_word = word

    def search(self, word: str) -> bool:
        temp = self.root
        for w in word:
            temp = temp.children.get(w)
            if not temp:
                return False
        return temp.the_word == True


class WordSearchII:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        res = []
        trie = Trie()
        root = trie.root

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res

    def dfs(self, board: List[List[int]], i: int, j: int, temp: TrieNode, res: List[str]) -> None:
        c = board[i][j]
        if c == '#' or not temp.children.get(c):
            return

        temp = temp.children.get(c)
        if temp.the_word:
            res.append(temp.the_word)
            temp.the_word = ""

        board[i][j] = '#'

        for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if i + dx >= 0 and i + dx < len(board) and j + dy >= 0 and j + dy < len(board[i]):
                self.dfs(board, i + dx, j + dy, temp, res)

        board[i][j] = c