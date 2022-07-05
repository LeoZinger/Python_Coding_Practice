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

        # test_digit1 = "abc"
        # test_digit2 = "def"
        # testRes = []
        # for letter in list(test_digit1):
        #     for x in list(test_digit2):
        #         testRes.append(letter + x)
        #     print("test res = ", testRes)

        for letter in [l for l in self.digitToLettersMap[digits[0]]]:
            print("letter=", letter)
            # print("recursive call returned list item = :", self.letterCombinations(digits[1:]))
            rest = self.letterCombinations(digits[1:])
            print("recursive call returned list item = : ", rest)

            if not rest:
                # res.append(letter)
                return [letter]
            else:
                for x in rest:
                    print("recursive call returned list item = : ", x)
                    res.append(letter + x)
                    print("res=", res)

            # for x in self.letterCombinations(digits[1:]):
            #     print("recursive call returned list item = : ", x)
            #     res.append(letter + x)
            #     print("res=", res)

        return res


str = "23"
solution = Solution()
print(solution.letterCombinations(str))