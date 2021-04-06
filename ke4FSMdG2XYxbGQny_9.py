
def even_odd_transform(lst, n):
    if sum(lst)==0:
        return [lst[i]+(-1)*2*n for i in range(0,len(lst))]
    else:
        x=[lst[i]+n*2*(-1) if (lst[i]%2==0) else lst[i]+(n)*(2) for i in range(0,len(lst))]
        return x

