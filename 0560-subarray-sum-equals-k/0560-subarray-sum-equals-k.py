class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, count  = 0, 0
        sums = defaultdict(int)
        sums[0] = 1
        for num in nums:
            prefix_sum += num
            count += sums[prefix_sum - k]
            sums[prefix_sum] += 1
        return count 