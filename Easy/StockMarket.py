class StockMarket:
    def maxProfit(self, prices):
        l, r = 0, 1
        maxP = 0
        
        #loop to compare prices
        while r < len(prices):
            #if left price is lt right price loop
            if prices[l] < prices[r]:
                #profit equals right price minus left
                profit = prices[r] - prices[l]
                #compare maxP vs profit and change max to the higher number
                maxP = max(maxP, profit)
            #if l=r shift increment and check
            else:
                l = r
            r += 1
        return maxP