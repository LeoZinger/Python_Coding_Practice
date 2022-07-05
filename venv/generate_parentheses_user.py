from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Notes:
            - Every open parenthesis needs to be closed. There cannot
            be more closed than open at any given time.
            - At every step/decision, there are two choices:
                1. If n is bigger than 0, you can add an open parenthesis.
                2. If there are open parenthesis, you can add a closed parenthesis.
        """
        self.result = []
        self.backtrack(combination="", curr_open=0, n=n)
        return self.result

    def backtrack(self, combination: str, curr_open: int, n: int) -> None:
        if n == 0 and curr_open == 0:
            self.result.append(combination)
            return
        if n > 0:
            self.backtrack(combination + "(", curr_open + 1, n - 1)
        if curr_open > 0:
            self.backtrack(combination + ")", curr_open - 1, n)


n = 3
solution = Solution()
print("End Result = ", solution.generateParenthesis(n))