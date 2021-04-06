
def k_th_binary_inlist(n, k):
    l = [bin(i) for i in range(2 ** n)]
    l = sorted(l, key=lambda x : x.count("1"), reverse=True)
    return l[k - 1]

