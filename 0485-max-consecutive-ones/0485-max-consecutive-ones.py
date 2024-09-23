class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        cmax=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                cmax=max(cmax,c)
            else:
                c=0
        return cmax 