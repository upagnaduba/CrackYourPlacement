class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        out=[0]*len(nums)
        stack=[nums[-1]]
        n=len(nums)
        for i in range(2*n-1,-1,-1):
            i%=n
            if stack[-1]>nums[i]:
                out[i]=stack[-1]
            else:
                while len(stack)>0 and stack[-1]<=nums[i]:
                    stack.pop()
                if len(stack)==0:
                    out[i]=-1
                else:
                    out[i]=stack[-1]
            stack.append(nums[i])
        return out
