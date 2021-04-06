
def k_th_binary_inlist(n, k):
  return sorted(list(map(lambda x: bin(x),range(0,pow(2,n)))), key = lambda y: y.count('1'),reverse = True)[k-1]

