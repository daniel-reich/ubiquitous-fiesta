
def k_th_binary_inlist(n, k):
    bi_list = [bin(b) for b in range(0, 2**n)]
    return sorted(bi_list, key=lambda x: x.count('1'), reverse=True)[k-1]

