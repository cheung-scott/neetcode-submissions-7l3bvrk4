class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = nums[0]
        for i, n in enumerate(nums):
            if n == res:
                count += 1
            else:
                count -= 1
                if count == 0:
                    res = nums[i]
                    count += 1
        return res
            