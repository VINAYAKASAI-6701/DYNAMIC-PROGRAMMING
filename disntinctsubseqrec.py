class Solution:
    def fun(self, s, t, i, j):
        # If we matched all of 't', return 1 valid way
        if j == -1:
            return 1

        # If 's' is exhausted before matching 't', return 0
        if i == -1:
            return 0

        if s[i] == t[j]:
            return self.fun(s, t, i - 1, j - 1) + self.fun(s, t, i - 1, j)
        else:
            return self.fun(s, t, i - 1, j)

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        return self.fun(s, t, n - 1, m - 1)

# Example
sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))  # Output: 3
