from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n  # Initialize DP array with 1 (every element is an LIS of length 1)
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:  # If increasing sequence found
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)  # Maximum LIS length
