from typing import List
from collections import Counter

class Solution:
    def moveNegativeElementsToEnd(self,arr: List[int]) -> List[int] :
        # Write your code here
        n = len(arr)
        if not arr or n == 0:
            return []
        left, right = 0, 0
        while right < n:
            if arr[right] < 0:
                if left < right:
                    if 0 <= arr[left]:
                        temp = arr[right]
                        arr[right] = arr[left]
                        arr[left] = temp
                        left += 1
                        right += 1
                    else:
                        left += 1
            else:
                right += 1
        return arr


solution = Solution()
arr = [1,1,-2,3,7,-5,12,-3,-5]
print("End Result = ", solution.moveNegativeElementsToEnd(arr))