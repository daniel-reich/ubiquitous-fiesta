
def spiral_order(arr):
    k = 0
    l = 0
    x=[]
    m=len(arr)
    n=len(arr[0])
    while (k < m and l < n):
        for i in range(l, n):
            x.append(arr[k][i])
        k+=1
        for i in range(k, m):
            x.append(arr[i][n - 1])
        n-=1
        if (k < m): 
            for i in range(n - 1, (l - 1), -1):
                x.append(arr[m - 1][i])
            m-=1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                x.append(arr[i][l] )
            l+=1
    return x

