class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = {}
        # {[i, s.count(i) for i in s]}
        
        for c in s:
                sMap[c] = sMap.get(c,0) + 1
        for c in t:
                sMap[c] = sMap.get(c,0) - 1

        return True if sMap.values() else False

solution = Solution()
s = "dog"
t = "god"
print("valid anagram?", solution.isAnagram(s,t))