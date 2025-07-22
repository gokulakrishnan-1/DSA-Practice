class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        curVal = 0
        maxVal = 0

        for key, values in counter.items():
            if values > curVal :
                curVal = values
                maxVal = key
        
        return maxVal
