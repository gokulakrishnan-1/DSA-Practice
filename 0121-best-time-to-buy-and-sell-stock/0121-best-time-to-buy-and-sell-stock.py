class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        r = 0

        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                if prices[r] - prices[l] > 0:
                    profit = max(profit, prices[r] - prices[l])
                else:
                    profit = 0
            else:
                l = r
            r += 1
        return profit

            



            
        