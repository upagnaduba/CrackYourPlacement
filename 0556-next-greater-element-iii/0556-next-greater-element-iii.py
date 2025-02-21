class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s=list(str(n))
        for i in range(len(s)):
            s[i]=int(s[i])
        ind=-1
        for i in range(len(s)-2,-1,-1):
            if s[i]<s[i+1]:
                ind=i
                break
        if ind==-1:
            return -1
        for i in range(len(s)-1,ind,-1):
            if s[i]>s[ind]:
                s[i],s[ind]=s[ind],s[i]
                break
        l=ind+1
        r=len(s)-1
        while(l<r):
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        s=map(str, s)
        s=''.join(s)
        n1=int(s)
        if n1> 2**31 - 1:
            return -1
        else:
            return n1