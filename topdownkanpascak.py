def knapsack_topdown(wt, val, n, cap):
    # Initialize DP table with 0
    t = [[0] * (cap + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for j in range(cap + 1):
            if wt[i - 1] <= j:  # Check if the item can be included
                pick = val[i - 1] + t[i - 1][j - wt[i - 1]]
                notpick = t[i - 1][j]
                t[i][j] = max(pick, notpick)
            else:
                t[i][j] = t[i - 1][j]

    return t[n][cap]  # Return the maximum value

# Example usage
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
n = len(wt)
capacity = 5

print(knapsack_topdown(wt, val, n, capacity))  # Output: 7
