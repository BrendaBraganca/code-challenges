class Solution(object):
    def maxProfit(self, prices):
        compra = prices[0]
        lucro = 0
        for i in range(1, len(prices)):
            if(prices[i] < compra):
                compra = prices[i]
            elif(prices[i] - compra > lucro):
                lucro = prices[i] - compra
        return lucro