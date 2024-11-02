class Solution(object):
    def makeFancyString(self, s):
        ans = []
        for i in s:
            if len(ans) < 2 or ans[-1] != i or ans[-2] != i:
                ans.append(i)
        return ''.join(ans)