class Solution(object):
    def isPalindrome(self, x):
       xr=str(x)
       rev=""
       for i in xr:
            rev=i+rev
       if rev==xr:
            return True
       else:
            return False
         
        