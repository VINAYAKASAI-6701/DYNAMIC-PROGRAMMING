from typing import List


class Solution:
    def countPartitions(self, arr, d):
        n=len(arr)
        s=sum(arr)
        if (s+d)%2!=0 or s<d:
            return 0
        target=(d+s)//2
        dp=[[0]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(target+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][target]
        # code here
        