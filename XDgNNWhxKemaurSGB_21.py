
def one_count(b):
    return b.count('1')
def k_th_binary_inlist(n, k):
    b=sorted([bin(i) for i in range(2**n)],reverse=True,key=lambda x:(one_count(x),-int(x,2)))
    return b[k-1]

