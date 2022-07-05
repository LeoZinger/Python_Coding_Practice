class Solution:
    def generateParentheses(self, n):
        if n == 0:
            return []
        if n == 1:
            return ["()"]

        bp = "("
        ep = ")"

        res = []
        count = 0
        i = 0
        while count <= n:
            temp_horizontal = ''
            while count <= n:
                temp_vertical = ''
                for j in range(i):
                    print("n=", n, end=" ")
                    count += 1
                    temp_vertical += ''.join(self.generateParentheses(n-count))
                i += 1
                temp_horizontal += bp + temp_vertical + ep
                print("temp_horizontal=", temp_horizontal)
            res.append(temp_horizontal)
            print("res=", res)
        return res


n = 3
solution = Solution()
print("End Result = ", solution.generateParentheses(n))
