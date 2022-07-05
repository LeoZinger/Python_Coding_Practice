class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return [[]]

        val = nums[0]
        results = []
        for subset in self.subsets(nums[1:]):
            results.append(subset)
            results.append([val] + subset)

        return results


nums = [0, 1, 2]
print(nums[1:])
solution = Solution()
print(solution.subsets(nums))
