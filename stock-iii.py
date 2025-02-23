class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def fun(prices,ind,buy,cap,n):
            if cap==0:return 0
            if ind==n:return 0
            profit=0
            if buy:
                return max(-prices[ind]+fun(prices,ind+1,0,cap,n),fun(prices,ind+1,1,cap,n))
            else:
                return max(prices[ind]+fun(prices,ind+1,1,cap-1,n),fun(prices,ind+1,0,cap,n))
        return fun(prices,0,1,2,len(prices))
