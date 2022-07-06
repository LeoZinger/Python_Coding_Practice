from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]

        minBananas = piles[-1] + 1
        count = 0
        k = right
        pre_k = float('inf')
        while k != pre_k:
            count += 1
            print("while left < right loop, left: ", left, ", right: ", right,  ", k (middle): ", k)
            hours = 0
            for i in range(len(piles)):
                hours += piles[i] // k if piles[i] % k == 0 else piles[i] // k + 1
                print("for i loop, i = ", i, " hours: ", hours)
                if hours > h:
                    print("Breaking out of for i loop, hours: ", hours, " > than h : ", h, " this i number: ", i, " doesn't work")
                    break   # this i number doesn't work
            if hours <= h: # found 1 solution with i number of bananas
                print("Found 1 solution with number of bananas (k) : ", k, ", breaking!")
                minBananas = k
                right = (k + len(piles)) // 2
                pre_k = k
                k = right
            else:
                left = (k + right) // 2
                pre_k = k
                k = left

        return minBananas


solution = Solution()
# piles = [3,6,7,11]
# h = 8
piles = [30,11,23,4,20]
h = 5
res = solution.minEatingSpeed(piles, h)
print("minBananas per hour: ", res)
