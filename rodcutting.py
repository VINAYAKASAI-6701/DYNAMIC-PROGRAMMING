class Solution:
    def cutRod(self, price):
        n=len(price)
        dp=[[0]*(n+1)for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i<=j:
                    dp[i][j]=max(price[i-1]+dp[i][j-i],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][n]
