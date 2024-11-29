class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        c=0
        odd=False
        for i in d:
            if d[i]%2==0:
                c+=d[i]
            else:
                c+=d[i]-1
                odd=True
        if odd:
            c+=1
        return c