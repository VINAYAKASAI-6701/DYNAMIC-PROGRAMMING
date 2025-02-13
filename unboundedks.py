class Solution:
    def knapSack(self, val, wt,capacity):
        if len(val)!=len(wt):
            return 0
        n=len(wt)
        #changing quantites matrix for cap and wt array-->unbounded kanpsack why bcz Note: Each item can be taken any number of times.
        dp=[[0]*(capacity+1)for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,capacity+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][capacity]
        # code here