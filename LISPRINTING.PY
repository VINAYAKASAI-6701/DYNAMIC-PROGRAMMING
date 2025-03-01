class Solution:
    def longestIncreasingSubsequence(self, N, arr):
        dp=[1]*N
        prev=[-1]*N
        for i in range(N):
            for j in range(i):
                if arr[i]>arr[j] and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    prev[i]=j
                    
        ele=max(dp)
        index=dp.index(ele)
        res=[]
        while index!=-1:
            res.append(arr[index])
            index=prev[index]
        return reversed(res)
