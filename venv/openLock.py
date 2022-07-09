from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lock = "0000"
        visited = set(deadends)
        def dfs(lock: List[str], minTurns: int) -> int:  # returns mininum turns
            if not lock or len(lock) == 0:
                return 0
            if lock not in visited:
                visited.add(lock)
                if lock == target:
                    return minTurns
            minNext = 0
            for i in range(4):
                minNext = min(minNext, dfs(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:], minTurns + 1))    #this won't work, total recusion depth (>1k)exceeding Python's max recursion depth (1000)
                minNext = min(minNext, dfs(lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i + 1:], minTurns + 1))

            return minNext + 1

        return dfs(lock, 0)


solution = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
res = solution.openLock(deadends, target)
print("mininum number of turns to open lock: ", res)
