class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        num=1
        nums.sort()
        for i in range(n):
            if nums[i]==num:
                num+=1
            elif nums[i]>num:
                break
        return num