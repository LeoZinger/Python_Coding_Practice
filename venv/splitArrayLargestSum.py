from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = sum(nums)
        print("divided by ", m, " of sum = ", n//m)

        arrSum = 0
        maxPartSum = 0
        partCount = 0
        i = 0
        while i < len(nums) and partCount <= m:
            arrSum += nums[i]
            if arrSum == n//m:
                print("arrSum == n, recording maxPartSum as max of ", arrSum, " and ", maxPartSum)
                maxPartSum = max(maxPartSum, arrSum)
                arrSum = 0
                partCount += 1
                i += 1
            elif arrSum > n//m:
                arrSum -= nums[i]
                print("arrSum > n, recording maxPartSum as max of ", arrSum, " and ", maxPartSum)
                maxPartSum = max(maxPartSum, arrSum)
                arrSum = nums[i]
                partCount += 1
                i += 1
        return maxPartSum
solution = Solution()
# nums = [7,2,5,10,8]
nums = [1,2,3,4,5]
m = 2

# nums = [1,4,4]
# m = 3
# correct res should be 18
# arr = [1,0,0,0,0,1]
# n = 2
res = solution.splitArray(nums, m)
print(res)



