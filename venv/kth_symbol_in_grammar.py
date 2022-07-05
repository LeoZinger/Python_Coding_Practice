class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        dp = [str] * (n)
        translate = {}
        translate['0'] = '01'
        translate['1'] = '10'
        dp[0] = '0'
        print(dp[0])
        for i in range(1,n):
            dp[i] = ''.join([translate[x] for x in dp[i-1]])
            print(dp[i])

        return dp[n-1][k-1]

n = 5
k = 2
solution = Solution()
print(f"kthGrammar({n},{k}) = ", solution.kthGrammar(n,k))