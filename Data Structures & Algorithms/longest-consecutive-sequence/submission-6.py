class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0
        for n in nums:
            count = 0
            current = 0
            if n - 1 not in numsSet:
                while n + current in numsSet:
                    current += 1
                    count += 1
                    maxCount = max(count, maxCount)
        return maxCount