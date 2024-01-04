from typing import List


def maxprofit(prices: List[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
        else:
            l = r
        r += 1
    return max_profit


print(maxprofit(prices=[7, 1, 5, 3, 6, 4]))
print(maxprofit(prices=[7, 6, 4, 3, 1]))