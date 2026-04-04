class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = r = 0
        deck = collections.deque()

        while r < len(nums):
            while deck and nums[deck[-1]] < nums[r]:
                deck.pop()
            deck.append(r)

            if l > deck[0]:
                deck.popleft()

            if r + 1 >= k:
                res.append(nums[deck[0]])
                l += 1
            r += 1
        return res    