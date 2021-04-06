
def min_length(lst, n):
  for i in range(1, len(lst)+1):
    for j in range(0, len(lst)):
      if sum(lst[j:j+i]) > n: return i
  return -1

