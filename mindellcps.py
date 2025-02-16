#User function Template for python3
class Solution:
    def minDeletions(self, Str, n): 
        s2=Str[::-1]
        n=len(Str)
        m=len(s2)
        dp=[[0]*(m+1)for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if Str[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][m]
        #code here