class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def fun(prices,ind,buy,k,n,dp):
            if ind==n or k==0:
                return 0
            if dp[ind][buy][k]!=-1:return dp[ind][buy][k]
            if buy:
                profit= max(-prices[ind]+fun(prices,ind+1,0,k,n,dp),fun(prices,ind+1,1,k,n,dp))
            else:
                profit= max(prices[ind]+fun(prices,ind+1,1,k-1,n,dp),fun(prices,ind+1,0,k,n,dp))
            dp[ind][buy][k]=profit
            return profit
        n=len(prices)
        #dp array 3d changing prameters ind,buy,k
        dp=[[[-1]* (k+1)for _ in range(2)]for _ in range(n)]
        return fun(prices,0,1,k,n,dp)
        
        