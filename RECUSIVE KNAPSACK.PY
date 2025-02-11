def knapsack(wt, val, n, cap):
    # Base case: If no items left or capacity is 0
    if n == 0 or cap == 0:
        return 0

    # If the current item's weight is greater than the remaining capacity, skip it
    if wt[n - 1] > cap:
        return knapsack(wt, val, n - 1, cap)
    
    # Pick or not pick the current item
    pick = val[n - 1] + knapsack(wt, val, n - 1, cap - wt[n - 1])  # Pick the item
    not_pick = knapsack(wt, val, n - 1, cap)  # Don't pick the item

    return max(pick, not_pick)

# Example usage
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
n = len(wt)
capacity = 5

print(knapsack(wt, val, n, capacity))  # Output: 7
