class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter as c
        d=c(nums)
        for i,j in d.items():
            if j>len(nums)//2:
                return i
                break
