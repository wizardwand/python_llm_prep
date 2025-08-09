from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        mp , min = 0, prices[0]
        for price in prices:
            if price < min:
                min = price
            else:
                mp = max(mp, price - min)
        return mp


profit = Solution().maxProfit([7, 1, 5, 3, 6, 4])
print(profit)
