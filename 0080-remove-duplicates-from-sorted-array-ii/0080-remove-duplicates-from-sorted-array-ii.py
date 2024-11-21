class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt={}
        for i in nums:
            if i in cnt:
                cnt[i]+=1
            else:
                cnt[i]=1
        k=0
        for i in nums:
            if cnt[i]==1:
                nums[k]=i
                k+=1
                cnt[i]=0
            elif cnt[i]>=2:
                nums[k],nums[k+1]=i,i
                k+=2
                cnt[i]=0
        return k
