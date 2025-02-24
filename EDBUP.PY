class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        # Step 1: Create a DP table initialized with 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Step 2: Base Case Initialization
        for i in range(n + 1):
            dp[i][0] = i  # Deleting all characters from word1
        for j in range(m + 1):
            dp[0][j] = j  # Inserting all characters into word1

        # Step 3: Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:  # No operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert_op = 1 + dp[i][j - 1]   # Insert character
                    delete_op = 1 + dp[i - 1][j]   # Delete character
                    replace_op = 1 + dp[i - 1][j - 1]  # Replace character
                    dp[i][j] = min(insert_op, delete_op, replace_op)

        # Step 4: Return the final answer
        return dp[n][m]
