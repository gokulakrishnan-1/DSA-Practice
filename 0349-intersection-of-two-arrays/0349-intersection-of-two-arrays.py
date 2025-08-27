class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num = set(nums1)
        ans = []
        for n in nums2:
            if n in num:
                ans.append(n)
                num.remove(n)
        return ans