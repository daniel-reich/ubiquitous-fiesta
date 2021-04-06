
def k_th_binary_inlist(n, k):
  return sorted(map(bin,range(2**n)),
         key=lambda x:(-x.count('1'),int(x,2)))[k-1]

