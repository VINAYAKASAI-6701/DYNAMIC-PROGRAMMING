import sys

def matrix_chain_recursive(arr, i, j, dp):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    
    min_cost = sys.maxsize
    
    for k in range(i, j):
        cost = (matrix_chain_recursive(arr, i, k, dp) +
                matrix_chain_recursive(arr, k + 1, j, dp) +
                arr[i - 1] * arr[k] * arr[j])
        
        min_cost = min(min_cost, cost)
    
    dp[i][j] = min_cost
    return dp[i][j]

# Example usage:
arr = [40, 20, 30, 10, 30]
n = len(arr)
dp = [[-1] * (n+1) for _ in range(n+1)]  # Corrected DP initialization
result = matrix_chain_recursive(arr, 1, n - 1, dp)
print("Minimum number of multiplications:", result)
