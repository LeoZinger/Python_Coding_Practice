from collections import Counter
class Solution:
    def countCharInStr(self, s: str, char: str) -> int:
        counts = Counter(s)
        #print(char, ":", counts.get(char))
        return counts.get(char)

s = "so many letters and slangs and characters"
char = "s"
solution = Solution()
countChar = solution.countCharInStr(s, char)
print(char, ":", countChar)
