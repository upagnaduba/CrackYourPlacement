class Solution(object):
    def findKthPositive(self, arr, k):
        nums=[]
        for i in range(1,len(arr)+k+1):
            if i not in arr:
                nums.append(i)
        return nums[k-1]