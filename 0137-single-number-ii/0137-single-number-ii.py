class Solution(object):
    def singleNumber(self, nums):
        counter=defaultdict(int)
        for i in nums:
            counter[i]+=1
        for num,freq in counter.items():
            if freq==1:
                return num
        