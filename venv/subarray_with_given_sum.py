from typing import List
class Solution:
    def subArraySum(self,arr: List[int], n: int, s: int) -> List[int] :
       # Write your code here
        if not arr or n == 0:
            return []
        res = []
        sum = 0
        left, right = 0, 0
        while right < n:
            if sum < s:
                sum += arr[right]
                right += 1
            elif sum == s:
                    print("sum = s, left = ", left, ", right = ", right)
                    res.append(left)
                    res.append(right)
                    return res
            else: # sum > s
                    sum -= arr[left]
                    left += 1
                    res.clear()

solution = Solution()
arr = [1,2,3,7,5]
n = len(arr)
s = 12
print("End Result = ", solution.subArraySum(arr, n, s))