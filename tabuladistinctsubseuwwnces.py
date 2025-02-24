class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)

        # Create DP table initialized with 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base Case: If t is empty, there is exactly 1 way (empty subsequence)
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, we can either include or exclude `s[i-1]`
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # If characters don't match, we can only exclude `s[i-1]`
                    dp[i][j] = dp[i - 1][j]

        return dp[n][m]

# Example usage
sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))  # Output: 3
