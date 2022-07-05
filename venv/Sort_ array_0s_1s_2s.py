class Solution:
    def sort012(self, arr, n):
        # code here
        if not arr or n == 0:
            return []
        freq = {}
        for i in range(n):
            if arr[i] == 0:
                freq[0] = freq.get(0,0) + 1
            elif arr[i] == 1:
                freq[1] = freq.get(1,0) + 1
            else:
                freq[2] = freq.get(2,0) + 1
        print("freq dict = ", freq)

        for i in range(n):
            if 0 <= i and i < freq[0]:
                arr[i] = 0
            elif freq[0] <= i and i < freq[0] + freq[1]:
                arr[i] = 1
            else:
                arr[i] = 2

        return arr

arr = [0,0,2,0,1,1,1,0,0,2,2,1,2,0,2,1,0,0,0]
print("orig arr, len = ", len(arr), " arr = ", arr)
solution = Solution()
solution.sort012(arr,len(arr))
print("Sorted arr len = ", len(arr), "by 0,1,2, arr = ", arr)
# {
#  Driver Code Starts
# Initial Template for Python 3

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         arr = [int(x) for x in input().strip().split()]
#         ob = Solution()
#         ob.sort012(arr, n)
#         for i in arr:
#             print(i, end=' ')
#         print()
#
# # } Driver Code Ends