# Declare a DP array globally
dp = [[-1 for _ in range(1001)] for _ in range(1001)]  # Assuming max string length is 1000

def lcs(x, y, n, m):
    if n == 0 or m == 0:
        return 0
    if dp[n][m] != -1:
        return dp[n][m]
    
    if x[n - 1] == y[m - 1]:
        dp[n][m] = 1 + lcs(x, y, n - 1, m - 1)
    else:
        dp[n][m] = max(lcs(x, y, n - 1, m), lcs(x, y, n, m - 1))
    
    return dp[n][m]

x = "abcdgh"
y = "abedfh"
n = len(x)
m = len(y)

# Reset DP array for current inputs (optional, if handling multiple test cases)
for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j] = -1

print(lcs(x, y, n, m))  # Output: 4 (LCS: "abdh")
