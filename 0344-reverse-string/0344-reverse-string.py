class Solution(object):
    def reverseString(self, s):
        n=len(s)
        for i in range(n//2):
            s[i],s[n-i-1]=s[n-i-1],s[i]
        return s
        