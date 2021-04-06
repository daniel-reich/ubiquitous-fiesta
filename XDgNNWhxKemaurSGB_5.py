
def k_th_binary_inlist(n, k):
    return  sorted([bin(a) for a in range(0, 2 ** n)], key= lambda x : x.count('1'), reverse= True)[k - 1]

