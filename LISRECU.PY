class Solution:
    def backtrack(self,ind,prev,nums):
        if ind==len(nums):
            return 0
        not_pick=self.backtrack(ind+1,prev,nums)
        pick=0
        if prev==-1 or nums[ind]>nums[prev]:
            pick=1+self.backtrack(ind+1,ind,nums)
        return max(pick,not_pick)
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        return self.backtrack(0,-1,nums)