class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=max(nums)
        CurMin,CurMax=1,1

        for n in nums:
            if n==0:
                CurMin,CurMax=1,1
                continue
            temp=n*CurMax
            CurMax=max(n*CurMin,n*CurMax,n)
            CurMin=min(n*CurMin,temp,n)
            
            result=max(result,CurMax)
        return result