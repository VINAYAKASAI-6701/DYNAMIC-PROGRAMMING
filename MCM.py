import sys

def matrix_chain_recursive(arr, i, j):
    if i >= j:
        return 0
    
    min_cost = sys.maxsize
    
    for k in range(i, j):
        cost = (matrix_chain_recursive(arr, i, k) +
                matrix_chain_recursive(arr, k + 1, j) +
                arr[i - 1] * arr[k] * arr[j])#extra cost
        
        min_cost = min(min_cost, cost)#first temp reesults
    
    return min_cost

# Example usage:
arr = [40, 20, 30, 10, 30]
n = len(arr)
result = matrix_chain_recursive(arr, 1, n - 1)
print("Minimum number of multiplications:", result)
