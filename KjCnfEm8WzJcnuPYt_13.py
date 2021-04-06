
def zero_indices(lst, k):
  for length in range(len(lst),0,-1):
    for i in range(len(lst)-length+1):
      part = lst[i:i+length]
      if part.count(0) <= k:
        return [i+j for j in range(len(part)) if part[j]==0]
  return []

