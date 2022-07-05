class Solution:
    def valid_anagram(self, s, t):
        if len(s) != len(t):
            return False
        t_dict, s_dict = dict.fromkeys(t, 0), dict.fromkeys(s, 0)
        print(t_dict)
        return t_dict == s_dict

solution = Solution()
s = "dog"
t = "god"
print("valid anagram?", solution.valid_anagram(s, t))
