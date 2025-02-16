class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #simple of variation of LCS finding secondstring and applying lcs function
        s2=s[::-1]
        n=len(s)
        m=len(s2)
        dp=[[0]*(m+1)for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]