
def matrix(n):
    a=[[1for i in range(n)]for i in range(n)];b=n//2;i=1
    while n>b:
        if i>1:
            a[-n][-n] = a[-n][-1 - n]+1
        for j in range(i,n):
            a[-n][j] = a[-n][j - 1]+1
        for j in range ( i, n ):
            a[j][n - 1] = a[j - 1][n - 1]+1
        for j in range ( i, n ):
            a[n-1][- 1-j] = a[n - 1][- j]+1
        for j in range(i,n-1):
            a[-1-j][-n] = a[-j][-n]+1
        i+=1;n-=1
    return a

