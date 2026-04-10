class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        maxCount = 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxCount = max(maxCount, r - l + 1)
            r += 1
        return maxCount