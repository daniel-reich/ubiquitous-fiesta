
def zero_indices(lst, k):
  ind = [i for i in range(len(lst)) if lst[i]==0]+[len(lst)]
  if len(ind)==k: return ind
  pot = [sum(lst[:ind[j+k]]) if j==0 else sum(lst[ind[j-1]:ind[j+k]]) for j in range(len(ind)-k)]
  x = pot.index(max(pot))
  return ind[x:x+k]

