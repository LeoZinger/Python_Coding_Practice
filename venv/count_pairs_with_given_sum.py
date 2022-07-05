class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        if not arr or n == 0:
            return 0
        pairs = {}
        count = 0
        for i in range(n):
            b = k - arr[i]
            if b in pairs:
                count += pairs[b]

            pairs[arr[i]] = pairs.get(arr[i], 0) + 1
        return count

solution = Solution()
arr = [1, 5, 7, 1]
n = 4
k = 6
print("End Result = ", solution.getPairsCount(arr, n, k))