class Solution(object):
    def findTheDifference(self, s, t):
        s=sorted(s)
        t=sorted(t)
        for i in range(len(t)-1):
            if s[i]!=t[i]:
                return t[i]
        return t[-1]