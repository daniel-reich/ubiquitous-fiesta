
def iqr(lst):
  L = sorted(lst,reverse=False) 
  child = len(L)//2 
  Q1,Q3 = 0,0 
  if child % 2==0: # even
    Q1 = (L[child//2-1]+L[child//2])/2
    Q3 = (L[child++len(L)%2+child//2-1]+L[child++len(L)%2+child//2])/2
  else:   
    Q1 = L[child//2]
    Q3 = L[child+child//2+len(L)%2]
  return Q3-Q1

