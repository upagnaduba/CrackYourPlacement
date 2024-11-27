class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        initial=0
        buy1=-inf
        sell1=0
        buy2=-inf
        sell2=0
        for x in prices:
            buy1=max(initial-x,buy1)
            sell1=max(buy1+x,sell1)
            buy2=max(sell1-x,buy2)
            sell2=max(buy2+x,sell2)
        return sell2