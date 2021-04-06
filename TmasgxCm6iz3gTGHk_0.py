
def min_length(lst, n):
  for i in range(1,len(lst)+1):
    for j in range(len(lst)-i+1):
      if sum(lst[j:i+j]) > n:
        return i
  return -1

