class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        n=len(arr)
        ind=-1
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                ind=i
                break
            
        if ind==-1:
            return arr.reverse()
        else:
            for i in range(n-1,ind,-1):
                if arr[i]>arr[ind]:
                    arr[i],arr[ind]=arr[ind],arr[i]
                    break
        l=ind+1
        r=n-1
        while(l<r):
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
            
        return arr