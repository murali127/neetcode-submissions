class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=len(nums)-nums.count(val)
        l,r=0,len(nums)-1
        while l<r:
            while l<r and nums[r]==val:
                r-=1
            if nums[l]==val:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            l+=1
        return k
