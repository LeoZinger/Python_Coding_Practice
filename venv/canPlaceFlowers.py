from typing import List
from collections import Counter
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1 and n == 1:
            return True if flowerbed[0] == 0 else False

        f_counter_list = Counter(flowerbed)
        print("Counter flowerbed = ", f_counter_list)
        print("Counter flowerbed.get(0) = ", f_counter_list.get(0))
        print("Counter flowerbed[0] = ", f_counter_list[0])
        if n > f_counter_list[0] / 2 + 1:
            return False

        m = len(flowerbed)
        print("len flowerbed = ", m)
        dp = [m + 1] * (m)
        # dp[0] = 0
        dp[0] = 1 if flowerbed[0] == 0 else 0
        dp[1] = 1 if flowerbed[0] == 0 and flowerbed[1] == 0 else 0
        cur_max = 0
        for i in range(2, m):
            if i < m-1:
                if (flowerbed[i] or flowerbed[i - 1] or flowerbed[i + 1]) == 1:
                    print("dp[", i, "] = ", dp[i])
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = max(dp[i - 1], dp[i - 2] + 1)
                    print("max dp[", i, "] = ", dp[i])
            else:
                 if (flowerbed[i] or flowerbed[i - 1]) == 1:
                    print("dp[", i, "] = ", dp[i])
                    dp[i] = dp[i - 1]
                 else:
                    dp[i] = max(dp[i - 1], dp[i - 2] + 1)
                    print("max dp[", i, "] = ", dp[i])

        print(dp)
        return True if dp[m - 1] >= n else False

# User correct Solution - Python Algorithmic
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         cnt = i = 0
#         while i < len(flowerbed):
#             if not flowerbed[i] == 1:
#                 left = 0 if i == 0 else flowerbed[i-1]
#                 right = 0 if i == len(flowerbed) - 1 else flowerbed[i+1]
#                 if left == 0 and right == 0:
#                     cnt += 1
#                     flowerbed[i] = 1
#             i += 1
#         return n <= cnt

solution = Solution()
arr = [1,0,0,0,0,0,1]
# arr = [1,0,0,0,0,1]
arr = [0,0,0]
n = 2
res = solution.canPlaceFlowers(arr, 2)
print(res)
