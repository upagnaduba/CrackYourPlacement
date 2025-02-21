class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i]==nums1[j]:
                    d[j]=i

        stack=[nums2[-1]]
        out=[0]*len(nums2)
        out[-1]=-1
        for i in range(len(nums2)-2,-1,-1):
            if stack[-1]>nums2[i]:
                out[i]=stack[-1]
                
            else:
                while len(stack)>0 and stack[-1]<=nums2[i]:
                    stack.pop()
                if len(stack)==0:
                    out[i]=-1
                else:
                    out[i]=stack[-1]
            stack.append(nums2[i])
        stack=[0]*len(nums1)
        for i,j in d.items():
            stack[i]=out[j]
        return stack
