class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def search_binary(stack,target):
            low=0
            high=len(stack)-1

            while low<=high:
                mid=(low+high)//2
                
                if stack[mid]>=target:
                    high=mid-1
                else:

                    low=mid+1
            stack.insert(low,target)
            return stack, low
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            removed_eles=[]
            stack,number_of_smallers=search_binary(stack,nums[i])
            nums[i]=number_of_smallers
        return nums