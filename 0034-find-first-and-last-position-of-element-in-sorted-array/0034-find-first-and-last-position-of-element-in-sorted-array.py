class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        a=[]
        for i in range(len(nums)):
            if nums[i]==target:
                a.append(i)
        if len(a)==0:
            return [-1,-1]
        else:
            return [a[0],a[-1]]