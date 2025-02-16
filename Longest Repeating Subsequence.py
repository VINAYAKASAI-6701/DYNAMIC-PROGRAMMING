#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, s):
	    s2=s
	    n=len(s)
	    m=len(s)
	    dp=[[0]*(m+1)for _ in range(n+1)]
	    for i in range(1,n+1):
	        for j in range(1,m+1):
	            if i!=j and s[i-1]==s2[j-1]:
	                dp[i][j]=1+dp[i-1][j-1]
	            else:
	                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
	    return dp[n][m]
		# Code here