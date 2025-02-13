class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1)for _ in range(n+1)]
        #1st row with intmax-1 
        for j in range(1,amount+1):
            dp[0][j]=float('inf')-1
        #second row because some may be having sums but size will be nothing 
        #i.e coins[0] if this divides amount(j) then ok otehrwise max value
        for j in range(1,amount+1):
            if j%coins[0]==0:
                dp[1][j]=j//coins[0]
            else:
                dp[1][j]=float('inf')-1
        #main code +1 for coin
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i][j-coins[i-1]]+1,dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][amount] if dp[n][amount] != float('inf') - 1 else -1

        
        