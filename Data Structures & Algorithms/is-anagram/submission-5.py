class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res1 = [0] * 26
        res2 = [0] * 26
        for i in range(len(s)):
            res1[ord(s[i]) - ord("a")] += 1
            res2[ord(t[i]) - ord("a")] += 1
        return res1 == res2
