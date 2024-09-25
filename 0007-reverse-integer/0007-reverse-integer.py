class Solution(object):
    def reverse(self, x):
            if x<0:
                x=-x
                x=str(x)
                rev=x[::-1]
                a=-int(rev)
                if a >= -2147483648 and a<= 2147483647 :
                    return a
                else:
                    return 0
            else:
                x=str(x)
                rev=x[::-1]  
                a=int(rev) 
                if a >= -2147483648 and a<= 2147483647 :
                    return a
                else:
                    return 0