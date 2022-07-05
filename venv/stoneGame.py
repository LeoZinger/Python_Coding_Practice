from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # countA, countB = 0, 0
        def dfs(piles: List[int], countA: int, countB: int, aPick: bool) -> bool:
            if not piles or len(piles) == 0:
                return countA > countB
            if aPick:
                return dfs(piles[1:], countA + piles[0], countB, False) and dfs(piles[:-1], countA + piles[-1], countB, False)
            else:
                return dfs(piles[1:], countA, countB + piles[0], True) and dfs(piles[:-1], countA, countB + piles[-1], True)

        return dfs(piles, 0, 0, True)


solution = Solution()
piles = [5, 3, 4, 5]
res = solution.stoneGame(piles)
print(res)
