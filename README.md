What is Dynamic Programming (DP)?
Dynamic Programming is an optimization technique used to solve problems by breaking them down into smaller subproblems, solving each subproblem once, and storing the result to avoid redundant computations.

Types of DP Approaches
1️⃣ Recursive Approach (Brute Force)

Solve the problem recursively by considering all possible choices.
Exponential time complexity (Worst case: O(2ⁿ)).
Leads to overlapping subproblems and redundant calculations.
2️⃣ Memoization (Top-Down DP)

Use recursion + caching to store already computed results.
Optimized recursive solution with O(N * Capacity) time complexity (for knapsack-type problems).
Reduces redundant calculations using a dictionary or an array.
3️⃣ Tabulation (Bottom-Up DP)

Solve the problem iteratively using a DP table.
Avoid recursion by solving smallest subproblems first and building up the solution.
Most optimized approach with O(N * Capacity) time complexity.
