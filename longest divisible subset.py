class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        #we need to sort this
        #just changing the code longest divisible subsequnce small chnage in code if LIS
        dp=[1]*n
        prev=[-1]*n
        nums.sort()
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0 and 1+dp[j]>dp[i]:
                    dp[i]=1+dp[j]
                    prev[i]=j
        n=max(dp)
        print(n)
        index=dp.index(n)
        res=[]
        while index!=-1:
            res.append(nums[index])
            index=prev[index]
        return res[::-1]
        