
def min_length(lst, n):
  for length in range(1, len(lst)+1):
    for subidx in range(len(lst)-length+1):
      if sum(lst[subidx:subidx+length]) > n:
        return length
  return -1

