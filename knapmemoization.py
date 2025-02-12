def knapsack(wt,val,n,capacity,dp):
    if n==0 or capacity==0:
        return 0
    if dp[n][capacity]!=-1:
        return dp[n][capacity]
    if wt[n-1]>capacity:
        dp[n][capacity]=knapsack(wt,val,n-1,capacity,dp)
    else:
        pick=val[n-1]+knapsack(wt,val,n-1,capacity-wt[n-1],dp)
        notpick=knapsack(wt,val,n-1,capacity,dp)
        dp[n][capacity]=max(pick,notpick)
    return dp[n][capacity]
wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
n = len(wt)
capacity = 5
dp=[[-1]*(capacity+1) for i in range(n+1)]
print(knapsack(wt,val,n,capacity,dp))