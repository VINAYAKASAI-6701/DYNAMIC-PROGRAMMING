class Solution:
    def longestCommonSubstr(self, s1, s2):
        #small varaiation from lonesgt common subsequence
        n,m=len(s1),len(s2)
        dp=[[0]*(m+1)for _ in range(n+1)]
        ml=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    ml=max(ml,dp[i][j])
                else:
                    dp[i][j]=0
        return ml