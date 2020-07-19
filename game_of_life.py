from typing import List

class GameOfLife:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        rows = len(board)
        cols = len(board[0])

        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = col + neighbor[1]

                    if r < rows and r >= 0 and c < cols and c >= 0 and copy_board[r][c] == 1:
                        live_neighbors += 1

                # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
                # Any live cell with more than three live neighbors dies, as if by over-population..
                if copy_board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0

                # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                if copy_board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1