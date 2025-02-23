from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            dp[ind][1] = max(-prices[ind] + dp[ind + 1][0], dp[ind + 1][1])
            dp[ind][0] = max(prices[ind] - fee + dp[ind + 1][1], dp[ind + 1][0])

        return dp[0][1]
