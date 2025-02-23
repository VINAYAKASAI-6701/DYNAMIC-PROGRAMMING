def getMaximumProfit(values, n):
    if n == 0:
        return 0

    dp = [[0] * 2 for _ in range(n + 1)]  

    for ind in range(n - 1, -1, -1):
        dp[ind][1] = max(-values[ind] + dp[ind + 1][0], dp[ind + 1][1])
        dp[ind][0] = max(values[ind] + dp[ind + 1][1], dp[ind + 1][0])

    return dp[0][1]

# Example Usage
values = [7, 1, 5, 3, 6, 4]
n = len(values)
print(getMaximumProfit(values, n))  # Output: 5
