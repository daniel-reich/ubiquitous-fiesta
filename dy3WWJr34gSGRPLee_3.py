
def make_box(n):
    a = []
    for i in range(1,n+1):
        if i == 1 or i == n:
            a.append("#"*n)
        elif 1<i<n:
            a.append("#"+" "*(n-2)+"#")
    return a

