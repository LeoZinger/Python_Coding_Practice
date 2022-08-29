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

def fib(n):
    # if n == 0 or n == 1:
    #     return 1
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 1
    print("dp[", 1, "] = ", dp[1])
    print("dp[", 2, "] = ", dp[2])
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print("dp[", i, "] = ", dp[i])
    # return fib(n-1) + fib(n-2)
    return dp[n]


fib_res = fib(100)
print("Fibonacci(n)", fib_res)