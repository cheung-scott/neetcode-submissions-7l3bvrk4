class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxCount = 0
        count = 0
        l = r = 0
        while r < len(s):
            if s[r] not in seen:
                count += 1
                seen.add(s[r])
                r += 1
                maxCount = max(maxCount, count)
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                seen.remove(s[l])                    
                l += 1
                count = r - l
                maxCount = max(maxCount, count)
        return maxCount
