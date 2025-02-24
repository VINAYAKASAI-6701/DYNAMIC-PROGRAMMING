class Solution:
    def fun(self,s,t,i,j,dp):
        #s2 i.e j reched negative means all are mathched
        if j==-1:
            return 1

        #s1 reached negative means s2 haent matched yet
        if i==-1:
            return 0

        if dp[i][j]!=-1:
            return dp[i][j]
        cnt=0
        if s[i]==t[j]:
            cnt=self.fun(s,t,i-1,j-1,dp)+self.fun(s,t,i-1,j,dp)
        
        else:
            cnt= self.fun(s,t,i-1,j,dp)
        dp[i][j]=cnt
        return cnt
    def numDistinct(self, s: str, t: str) -> int:
        #just think of recursion first
        n=len(s)
        m=len(t)
        dp=[[-1]*(m+1)for _ in range(n+1)]
        return self.fun(s,t,n-1,m-1,dp)
        
        