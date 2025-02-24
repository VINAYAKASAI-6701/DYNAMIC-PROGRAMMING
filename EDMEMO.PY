class Solution:
    def fun(self,i,j,dp,s1,s2):
        if i<0:
            return j+1
        
        if j<0:
            return i+1

        if dp[i][j]!=-1:
            return dp[i][j]

        if s1[i]==s2[j]:
            dp[i][j]= self.fun(i-1,j-1,dp,s1,s2)#0 opertaions
        else:
            ins=1+self.fun(i,j-1,dp,s1,s2)
            dele=1+self.fun(i-1,j,dp,s1,s2)
            rep=1+self.fun(i-1,j-1,dp,s1,s2)
            dp[i][j]=min(ins,dele,rep)
        return dp[i][j]


    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*(m)for _ in range(n)]
        return self.fun(n-1,m-1,dp,word1,word2)
        