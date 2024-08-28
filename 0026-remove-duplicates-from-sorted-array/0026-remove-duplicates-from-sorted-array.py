class Solution(object):
    def removeDuplicates(self, nums):
        cnt=[]
        k=0        
        for i in nums:             
            if i not in cnt:                 
                cnt.append(i)                 
                nums[k]=i                 
                k+=1
        return k
        