class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        d={}
        n=len(arr)
        
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        L=[]
        
        for item,val in d.items():
            if val>n//3:
                L.append(item)
        L.sort()
        return L