class Solution(object):
    def maxProfit(self, prices):
        buy=prices[0]
        maxp=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]<buy:
                buy=prices[i]
            elif (prices[i]-buy)>maxp:
                maxp=prices[i]-buy
        return maxp

        