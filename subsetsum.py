class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        t = [[False] * (target + 1) for _ in range(n + 1)]  # Initialize DP table
        
        # Base conditions
        for i in range(n + 1):
            t[i][0] = True  # Sum 0 is always possible with an empty subset
        
        for j in range(1, target + 1):
            t[0][j] = False  # Non-zero sum is not possible with 0 elements

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] <= j:
                    t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
                else:
                    t[i][j] = t[i - 1][j]

        return t[n][target]


# Driver code to test the function
if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    target = 9
    solution = Solution()
    result = solution.isSubsetSum(arr, target)
    
    if result:
        print("Subset with the given sum exists.")
    else:
        print("No subset with the given sum found.")
