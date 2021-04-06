
def k_th_binary_inlist(n, k):
    a = [bin(i) for i in range(2 ** n)]
    a = sorted(a, key=lambda x: (x.count("1"), -int(x,2)), reverse=True)
    return a[k-1]

