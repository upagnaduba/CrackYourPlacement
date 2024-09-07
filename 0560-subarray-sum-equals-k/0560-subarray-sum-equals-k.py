class Solution(object):
    def subarraySum(self, nums, k):
        res=0
        currsum=0
        prefixsum={0:1}
        for n in nums:
            currsum+=n
            diff=currsum-k
            if diff in prefixsum:
                res+=prefixsum[diff]
            if currsum in prefixsum:
                prefixsum[currsum]+=1
            else:
                prefixsum[currsum]=1
        return res
        