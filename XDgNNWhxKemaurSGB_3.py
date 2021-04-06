
def k_th_binary_inlist(n, k):
  return sorted([bin(i) for i in range(2**n)], key=lambda bn:len(bn.replace('0', '')), reverse=True)[k-1]

