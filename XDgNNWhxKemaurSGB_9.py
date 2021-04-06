
def k_th_binary_inlist(n, k):
  return sorted([bin(i) for i in range((2**n - 1)+1)],key=lambda x: x.count('1'),reverse=True)[k-1]

