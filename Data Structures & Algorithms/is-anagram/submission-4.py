class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26    
        for n in range(len(s)):
            freq1[ord(s[n]) - ord("a")] += 1
            freq2[ord(t[n]) - ord("a")] += 1
        return freq1 == freq2


            


