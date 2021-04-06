
def k_th_binary_inlist(n, k):
    return sorted([bin(num) for num in range(2**n)], key=lambda item: (item.count('1')), reverse=True)[k-1]

