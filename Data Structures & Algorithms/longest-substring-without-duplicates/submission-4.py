class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxCount = 0
        l = r = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            count = r - l 
            maxCount = max(count, maxCount)
        return maxCount

