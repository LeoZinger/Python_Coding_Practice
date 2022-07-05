# combine(a, b)
# takes in two combinations a and b and generate x.
# Just pass x to the next combine call and problem is solved.

class Solution:
    def combine(self, combination1, combination2):
        res = []

        for c in combination1:
            for alt_c in combination2:
                res.append(c + alt_c)

        return res

    def letterCombinations(self, digits):

        if len(digits) == 0:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        if len(digits) == 1:
            for c in mapping[digits[0]]:
                res.append(c)
            return res

        res = self.combine(mapping[digits[0]], mapping[digits[1]])

        for digit in digits[2:]:
            res = self.combine(res, mapping[digit])

        return res

str = "235"
solution = Solution()
print(solution.letterCombinations(str))