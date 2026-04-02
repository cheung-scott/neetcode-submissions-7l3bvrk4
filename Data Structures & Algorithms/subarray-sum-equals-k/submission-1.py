class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        total = 0
        count = 0
        for n in nums:
            total += n
            diff = total - k            
            
            count += prefixSums.get(diff, 0)
            prefixSums[total] = 1 + prefixSums.get(total, 0)
        return count




        