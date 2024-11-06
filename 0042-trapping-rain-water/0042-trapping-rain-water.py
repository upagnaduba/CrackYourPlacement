class Solution(object):
    def trap(self, height):
        lm=[0]*len(height)
        rm=[0]*len(height)
        lm[0]=height[0]
        rm[-1]=height[-1]
        for i in range(1,len(height)):
            lm[i]=max(height[i],lm[i-1])
        for i in range(len(height)-2,-1,-1):
            rm[i]=max(rm[i+1],height[i])
        trappedwater=0
        for i in range(len(height)):
            mini=min(lm[i],rm[i])
            trappedwater+=mini-height[i]
        return trappedwater

        