
def k_th_binary_inlist(n, k):
  a=[bin(i)  for i in range (2**n)]
  b=sorted (a, key =lambda x : x.count("1"),reverse =True)
  return b[k-1]

