
def bell(n):
  seq = [1]
  for i in range (n-1):
    seq = [1]+[seq[j-1]+(j+1)*seq[j] for j in range (1,len(seq))]+[1]
  return sum(seq)

