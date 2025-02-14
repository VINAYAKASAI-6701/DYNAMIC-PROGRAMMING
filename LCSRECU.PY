def lcs(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        return 1+lcs(x,y,n-1,m-1)
    else:
        pick_x=lcs(x,y,n-1,m)
        pick_y=lcs(x,y,n,m-1)
        return max(pick_x,pick_y)

x='abcdgh'
y='abedfh'
n=len(x)
m=len(y)
print(lcs(x,y,n,m))