
def n_differences(lst):
  l = lst
  
  while len(l) != 1:
    l = [l[i+1]-l[i] for i in range(len(l)-1)]
  return l[0]

