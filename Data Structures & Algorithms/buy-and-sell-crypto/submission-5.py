class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # purchase date. if the price is lower, then we buy on that date. if the price is higher then we sell on that date. purchase date must always be before selling date.
        # Maybe we can find the max value and then the minum value before the max value
        MaxP = 0
        MinB = prices[0]

        for price in prices:
            MaxP = max(MaxP, price - MinB)
            MinB = min(MinB, price)
        

        return MaxP
 


        