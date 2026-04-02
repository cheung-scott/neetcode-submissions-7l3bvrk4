class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0
        output = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in seen:
                while nums[i] + count in seen:
                    count += 1
                output = max(count, output)
                count = 0
        return output
