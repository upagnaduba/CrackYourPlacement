class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            s=s[1:]+s[0]
            if goal==s:
                return True
        return False
        