def fib(n, dp):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if dp[n] != -1:
        return dp[n]  # Use the previously computed value

    # Recursively calculate and store the result in dp[n]
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return dp[n]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    dp = [-1] * (n + 1)  # Initialize the DP array with -1
    print(f"Fibonacci({n}) =", fib(n, dp))
