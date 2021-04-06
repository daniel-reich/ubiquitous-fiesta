
def generate_nonconsecutive(n):
  A=[bin(x)[2:].zfill(n) for x in range(2**n)]
  B=[x for x in A if all(int(x[i])*int(x[i+1])==0 for i in range(len(x)-1))]
  return ' '.join(B)

