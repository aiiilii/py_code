class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        to_add = 0
        if player == 1:
            to_add = 1
        else:
            to_add = -1

        self.rows[row] += to_add
        self.cols[col] += to_add

        if row == col:
            self.diagonal += to_add
        if row + col == self.n - 1:
            self.anti_diagonal += to_add

        if self.n * to_add in [self.rows[row], self.cols[col], self.diagonal, self.anti_diagonal]:
            return player

        return 0