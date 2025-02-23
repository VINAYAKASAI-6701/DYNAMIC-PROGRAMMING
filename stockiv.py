class Solution:
    def fun(self,ind,buy,n,prices,dp):
        if ind>=n:
            return 0
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        profit=0
        if buy:
           profit= max(-prices[ind]+self.fun(ind+1,0,n,prices,dp),self.fun(ind+1,1,n,prices,dp))
        else:
           profit= max(prices[ind]+self.fun(ind+2,1,n,prices,dp),self.fun(ind+1,0,n,prices,dp))
        dp[ind][buy]=profit
        return profit
    def maxProfit(self, prices: List[int]) -> int:
        #minor change after sell in function
        n=len(prices)
        dp=[[-1]*(2)for _ in range(n)]
        return self.fun(0,1,n,prices,dp)