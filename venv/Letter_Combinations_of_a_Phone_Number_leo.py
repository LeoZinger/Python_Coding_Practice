from typing import List
class Solution:
    digitToLettersMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                         "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
                         }
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        def helper(combination: str, remaining: str) -> None:
            print("\n")
            print("helper: combination:", combination, " remaining:", remaining)
            if not remaining or len(remaining) == 0:
                res.append(combination)
                print("stopping. appended res combination:", combination, " remaining:", remaining)
            else:
                print("else: remaing[0]:", remaining[0])
                for letter in self.digitToLettersMap[remaining[0]]:
                    combination += letter
                    print("for loop: combination:", combination, " remaining:", remaining[1:])
                    helper(combination, remaining[1:])

        helper("", digits)
        return res

str = "23"
solution = Solution()
print(solution.letterCombinations(str))