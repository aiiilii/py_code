import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        temp = self.root
        for w in word:
            temp = temp.children[w]
        temp.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        temp = self.root
        self.res = False
        self.dfs(temp, word)
        return self.res


    def dfs(self, node: TrieNode, word: str) -> None:
        if not word: # if word finished,
            if node.is_word: # and node.is_word is true, then set self.res = true
                self.res = True
            return # return even if node.is_word is false, as long as word is finished

        if word[0] == '.':
            for n in node.children.values():
                self.dfs(n, word[1:]) # always exclude the first letter, thus the next round word[0] refers to the next letter
        else:
            node = node.children.get(word[0])
            if not node: # if the next node is not there, then return
                return
            self.dfs(node, word[1:])