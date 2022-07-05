class Solution:
    digitToLettersMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
                         }

    def letterCombinations(self, digits):
        if not digits or len(digits) == 0:
            if len(digits) == 0:
                print("return empty str")
            return []
        print("digits = ", digits)
        res = []

        print("digits[0]=", digits[0])
        print("digits[1:]=", digits[1:])

        print("letters=", end="")
        for letter in [l for l in self.digitToLettersMap[digits[0]]]:
            print(letter, end=" ")
            # print("recursive call returned list item = :", self.letterCombinations(digits[1:]))
            return letter+x if self.letterCombinations(digits[1:]) else letter



str = "23"
solution = Solution()
print(solution.letterCombinations(str))