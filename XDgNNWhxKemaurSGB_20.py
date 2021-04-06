
def k_th_binary_inlist(n, k):
  A=[bin(x) for x in range(2**n)]
  B=sorted(A, key=lambda x: (x.count('1'), -int(x,2)), reverse=True)
  return B[k-1]

