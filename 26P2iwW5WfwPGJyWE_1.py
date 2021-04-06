
def possibly_perfect(k, a):
  return len(set(i==j for i,j in zip(k,a) if i!="_"))==1

