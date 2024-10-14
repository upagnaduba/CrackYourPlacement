# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high=n
        low=1
        while(low<high):
            mid=(low+high)//2
            if isBadVersion(mid):
                high=mid
            else:
                low=mid+1
        return low