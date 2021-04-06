
def zero_indices(lst, k):
  for i in range(len(lst)-1,-1,-1):#len of one
    for j in range(len(lst)-i+1):#start idx
      mem=lst[j:j+i]
      if mem.count(0)==k:
        return [j+k for k in range(i) if not mem[k]]

