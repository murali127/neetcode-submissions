class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter as c
        b=c(nums)
        for j in b.values():
            if j>1:
                return True
        return False