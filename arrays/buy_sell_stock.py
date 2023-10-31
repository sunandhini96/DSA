# Problem Statement: 

## You are given an array prices where prices[i] is the price of a given stock on the ith day.

## You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

## Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


