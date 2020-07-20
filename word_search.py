from typing import List

class WordSearch:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        for row in range(self.rows):
            for col in range(self.cols):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row: int, col: int, word: str) -> bool:
        # word is begin copied frm [1:], so it's length will decrease
        # once it decreased to 0, means all letters of the word has been found
        if len(word) == 0:
            return True

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.board[row][col] != word[0]:
            return False

        self.board[row][col] = '#'

        for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            if self.backtrack(row + dx, col + dy, word[1:]): # so word[0] always refers to the current index
                return True

        self.board[row][col] = word[0]

        return False