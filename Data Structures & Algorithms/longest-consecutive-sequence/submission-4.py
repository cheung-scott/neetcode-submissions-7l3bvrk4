class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxCount = 0
        for n in nums:
            count = 0
            if n - 1 not in numsSet:
                while n + count in numsSet:
                    count += 1
                maxCount = max(count, maxCount)
        return maxCount