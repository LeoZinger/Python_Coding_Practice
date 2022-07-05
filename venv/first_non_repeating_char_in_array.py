from typing import List
from collections import Counter

class Solution:
    def firstNonRepeatingChar(self,arr: List[int]) -> int :
        # Write your code here
        n = len(arr)
        if not arr or n == 0:
            return float('-inf')
        res = float('-inf')
        counter_dict = Counter(arr)
        for k in counter_dict.keys():
            if counter_dict[k] == 1:
                return k
        return res


solution = Solution()
arr = [1,1,2,3,7,5,2,3,5]
print("End Result = ", solution.firstNonRepeatingChar(arr))