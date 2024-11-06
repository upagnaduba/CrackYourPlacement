class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxa=0
        while(l<r):
            area=(min(height[l],height[r]))*(r-l)
            maxa=max(maxa,area)
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
        return maxa


        