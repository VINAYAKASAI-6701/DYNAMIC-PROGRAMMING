class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        s=sum(nums)
        #similar to countprtition subsetsum1-subsetsum counts equal to difernce
        t=(s+target)//2
        if (s+target)%2!=0 or s<abs(target):
            return 0
        dp=[[0]*(t+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(t+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][t]

