from collections import deque

class RottingOranges:
    
    # use all rotten orange as start position
    # use count to count the number of 1 (fresh oranges), when one fresh orange become rotton, count -= 1
    # once bfs is over, count should be 0 if all fresh oranges are rotten
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        days = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (0 <= x < m) and (0 <= y < n) and grid[x][y] == 1:
                        grid[x][y] = 2
                        count -= 1
                        queue.append((x, y))
            days += 1

        if count == 0:
            return max(0, days - 1) # return res -1 because the final iteration of the while loop runs for orange/oranges that are already rotten and don't have any fresh neighbours (so no time consumed)
        else:
            return -1