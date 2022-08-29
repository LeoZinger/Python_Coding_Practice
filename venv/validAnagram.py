import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = {}
        # {[i, s.count(i) for i in s]}
        # tMap = {}
        # {[i, s.count(i) for i in t]}

        # for c in s:
        #     sMap[c] = sMap.get(c, 0) + 1
        # for c in t:
        #     sMap[c] = sMap.get(c, 0) - 1
        # print(sMap)
        # return sMap.values()

        return collections.Counter(s) == collections.Counter(t)

solution = Solution()
s="anagram"
t="nagaram"
# s = "rat"
# t = "car"
res = solution.isAnagram(s, t)
print("isAnagram : ", res)