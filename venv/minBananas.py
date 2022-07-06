from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            pivot = (l + r) // 2
            if sum([math.ceil(val/pivot) for val in piles]) <= h: # condition that checks if this pivot = k val works out
                r = pivot - 1
            else:
                l = pivot + 1
        return l

solution = Solution()
piles = [3,6,7,11]
h = 8
# piles = [30,11,23,4,20]
# h = 5
res = solution.minEatingSpeed(piles, h)
print("minBananas per hour: ", res)
