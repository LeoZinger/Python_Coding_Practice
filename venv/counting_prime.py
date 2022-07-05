class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0

        prime = [True] * (n)

        prime[0] = False
        prime[1] = False

        for i in range(2, n):
            if prime[i]:
                for j in range(i ** 2, n, i):
                    prime[j] = False

        # print(prime)

        count = 0

        for ele in prime:
            if ele:
                count += 1

        return count


solution = Solution()
n = 10
print("End Result = ", solution.countPrimes(10))