
k_th_binary_inlist = lambda n, k: sorted([bin(b) for b
    in range((1 << n))], key=lambda x: -x.count('1'))[k-1]

