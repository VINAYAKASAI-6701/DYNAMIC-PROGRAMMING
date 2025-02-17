def fib(n,dp):
    if n<=0:
        return 0
    if n==1:
        return 1
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

    
n=int(input("enter num"))
dp=[-1]*(n+1)
print(fib(n,dp))