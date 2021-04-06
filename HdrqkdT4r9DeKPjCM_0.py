
def is_polygonal(n):
    if n == 1: return '0th of all'
    k = 2*(n-1); maxi = int((k/3)**0.5); r =[]
    for i in range(maxi+1,1,-1):
        if k % i == 0 and (k//i) % (i-1) == 0 and k//i//(i-1) >= 3: r.append([i-1, k//i//(i-1)])
    for i in range(len(r)): j=r[i][0]; r[i]=[str(j)+['st 'if str(j)[-1]=='1' and j!=11 else'nd '
        if j==2 else'rd 'if j==3 else 'th '][0]+str(r[i][1])+"-gonal number"]
    return False if len(r) == 0 else [i[0] for i in r]

