
def k_th_binary_inlist(n, k):
  numb=list()
  numb2=list()
  for i in range(2**n):
    count=str(bin(i)).count('1')
    numb.append([-count,i,bin(i)])
  numb.sort()
  for i in numb:
    numb2.append(i[2])
  return numb2[k-1]

