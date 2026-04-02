class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for n in s:
            if n.isalnum():
                cleaned += n.lower()

        l, r = 0, len(cleaned) - 1
        while l < r:
            if cleaned[l] != cleaned[r]:
                return False
            else:
                l += 1
                r -= 1
        return True