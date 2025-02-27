class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s+=i
        n=len(nums)
        expeced_s=n*(n+1)/2
        return int(expeced_s-s)