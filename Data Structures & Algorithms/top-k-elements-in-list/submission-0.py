class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        heap = [(-freq, nums) for (nums, freq) in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for n in range(k)]