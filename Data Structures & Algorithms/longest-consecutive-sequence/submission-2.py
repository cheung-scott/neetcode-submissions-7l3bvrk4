class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in numsSet:
                count = 0
                while n + count in numsSet:
                    count += 1
                longest = max(longest, count)
        return longest