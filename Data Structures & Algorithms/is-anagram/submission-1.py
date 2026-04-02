class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        if len(s) != len(t):
            return False
        for n in s:
            if n not in seen1:
                seen1[n] = seen1.get(n, 0)
            else:
                seen1[n] = seen1.get(n, 0) + 1
        for n in t:
            if n not in seen2:
                seen2[n] = seen2.get(n, 0)
            else:
                seen2[n] = seen2.get(n, 0) + 1
        if seen1 == seen2:
            return True
        else:
            return False