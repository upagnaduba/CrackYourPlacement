class Solution(object):
    def maxProfit(self, prices):
        maxp=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                maxp=maxp+prices[i+1]-prices[i]
        return maxp