from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        for row in range(len(grid)):
            # print("nums row = ", row)
            for col in range(len(grid[row])):
                # print("nums col = ", col)
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append([row, col])
        # print("Initial Fresh = ", fresh)
        # print("Initial q = ", q)
        if fresh == 0:
            return 0

        minutes = 0
        adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                # print("minutes = ", minutes)
                # print("q popped grid[",row,"][",col,"] = ", grid[row][col])
                for r, c in adjacent:
                    if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[row]):
                        if grid[row+r][col+c] == 1:
                            # print("Adjacent fresh grid[", row+r, "][", col+c, "] = ", grid[row+r][col+c], " rotting")
                            grid[row+r][col+c] = 2
                            fresh -= 1
                            q.append([row + r, col + c])

            minutes += 1
        return minutes if fresh == 0 else -1


solution = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
res = solution.orangesRotting(grid)
print("mininum number of minutes until all oranges are rotten : ", res)