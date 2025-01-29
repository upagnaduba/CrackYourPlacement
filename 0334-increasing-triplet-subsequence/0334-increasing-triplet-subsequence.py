class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minl=[0]*len(nums)
        minl[0]=nums[0]
        maxl=[0]*len(nums)
        maxl[-1]=nums[-1]
        for i in range(1,len(nums)):
            minl[i]=min(minl[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            maxl[i]=max(maxl[i+1],nums[i])
        for i in range(1,len(nums)-1):
            if minl[i]<nums[i]<maxl[i]:
                return True
        return False