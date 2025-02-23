class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def fun(prices,ind,buy,cap,n,dp):
            if cap==0:return 0
            if ind==n:return 0
            if dp[ind][buy][cap]!=-1:
                return dp[ind][buy][cap]
            profit=0
            if buy:
                profit= max(-prices[ind]+fun(prices,ind+1,0,cap,n,dp),fun(prices,ind+1,1,cap,n,dp))
            else:
                profit=max(prices[ind]+fun(prices,ind+1,1,cap-1,n,dp),fun(prices,ind+1,0,cap,n,dp))
            dp[ind][buy][cap]=profit
            return profit
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)]for _ in range(n)]
        return fun(prices,0,1,2,len(prices),dp)

        