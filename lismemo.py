class Solution:
    def backtrack(self,ind,prev,nums,dp):
        if ind==len(nums):
            return 0
        if dp[ind][prev]!=-1:
            return dp[ind][prev]
        not_pick=self.backtrack(ind+1,prev,nums,dp)
        pick=0
        if prev==-1 or nums[ind]>nums[prev]:
            pick=1+self.backtrack(ind+1,ind,nums,dp)
        dp[ind][prev]=max(pick,not_pick)
        return dp[ind][prev]
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        return self.backtrack(0,-1,nums,dp)