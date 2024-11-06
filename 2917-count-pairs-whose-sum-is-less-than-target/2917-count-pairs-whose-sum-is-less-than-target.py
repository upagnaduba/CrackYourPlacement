class Solution(object):
    def countPairs(self, nums, target):
        l=0
        r=len(nums)-1
        nums.sort()
        count=0
        while(l<r):
            if(nums[l]+nums[r]<target):
                count+=r-l
                l+=1
            else:
                r-=1
        return count
        