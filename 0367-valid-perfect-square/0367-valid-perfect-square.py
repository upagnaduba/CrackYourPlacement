class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<1:
            return false
        left=1
        right=num
        while left<=right:
            mid=left+(right-left)//2
            if mid*mid==num:
                return True
            if mid*mid<num:
                left=mid+1
            else:
                right=mid-1
        return False