class Solution:
    def fun(self,ind,buy,prices,dp,fee):
        if ind==len(prices):
            return 0
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        profit=0
        if buy:
            profit=max(-prices[ind]+self.fun(ind+1,0,prices,dp,fee),self.fun(ind+1,1,prices,dp,fee))
        else:
            profit=max(prices[ind]-fee+self.fun(ind+1,1,prices,dp,fee),self.fun(ind+1,0,prices,dp,fee))
        
        dp[ind][buy]=profit
        return profit

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        return self.fun(0,1,prices,dp,fee)
        