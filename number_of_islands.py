class NumberOfIslands:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.callDFS(grid, i, j)

        return count

    def callDFS(self, grid: List[List[str]], i: int, j: int):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0' or grid[i][j] == '2':
            return;

        grid[i][j] = '2'
        self.callDFS(grid, i + 1, j)
        self.callDFS(grid, i - 1, j)
        self.callDFS(grid, i, j + 1)
        self.callDFS(grid, i, j - 1)