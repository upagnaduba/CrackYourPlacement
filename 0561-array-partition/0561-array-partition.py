class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        s=0
        for i in range(0,len(nums),2):
            s+=nums[i]
        return s
        