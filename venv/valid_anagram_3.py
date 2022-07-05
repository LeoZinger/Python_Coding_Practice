class Solution:
    def valid_anagram(self, s, t):
        if len(s) != len(t):
            return False
        uniq = set(s)

        for c in uniq:
            if s.count(c) != t.count(c):
                return False

        return True


solution = Solution()
s = "dog"
t = "god"
print("valid anagram?", solution.valid_anagram(s,t))
