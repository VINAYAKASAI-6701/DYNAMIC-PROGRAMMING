class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct LCS string
        i, j = n, m
        lcs_str = []
        
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:  # If characters match
                lcs_str.append(text1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move in the direction of max value
                i -= 1
            else:
                j -= 1

        lcs_str.reverse()  # Since we added characters in reverse order
        lcs_final = "".join(lcs_str)

        print(f"LCS: {lcs_final}")  # Print LCS string
        return dp[n][m]  # Return LCS length

# Example usage
sol = Solution()
print("LCS Length:", sol.longestCommonSubsequence("abcde", "ace"))  # Output: LCS = "ace", Length = 3
