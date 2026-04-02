class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        if len(s) != len(t):
            return False
        for n in s:
            seen1[n] = seen1.get(n, 0) + 1
        for n in t:
            seen2[n] = seen2.get(n, 0) + 1
        return seen1 == seen2