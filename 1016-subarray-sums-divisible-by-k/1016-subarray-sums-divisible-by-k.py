class Solution(object):
    def subarraysDivByK(self, nums, k):
        res=0
        prefixsum=0
        countmap={0:1}
        for n in nums:
            prefixsum+=n
            rem=prefixsum%k
            if rem in countmap:
                res+=countmap[rem]
                countmap[rem]+=1
            else:
                countmap[rem]=1
        return res
        