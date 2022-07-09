from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lock = "0000"
        if lock in deadends:
            return -1
        visited = set(deadends)
        q = deque()
        q.append(("0000", 0))

        def children(lock: str) -> List[str]:
            res = []
            for i in range(4):
                res.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:])
                res.append(lock[:i] + str((int(lock[i]) - 1 + 10) % 10) + lock[i + 1:])
            return res

        while q:
            lock, numTurns = q.popleft()
            if lock == target:
                return numTurns
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, numTurns + 1))
        return -1

solution = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
res = solution.openLock(deadends, target)
print("mininum number of turns to open lock: ", res)
