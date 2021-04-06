
def euclidean(a, b):
  r=[i for i in range(1,a+1) if a%i==0]
  g=[j for j in range(1,b+1) if b%j==0]
  v=list(set(r).intersection(set(g)))
  return max(v)

