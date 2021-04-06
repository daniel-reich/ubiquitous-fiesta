
def k_th_binary_inlist(n, k):
  return sorted([bin(i) for i in range(0, 2**n)], key=lambda x: -x.count('1'))[k-1]

