
def min_length(lst, n):
  res = sorted([j-i for i in range(len(lst)) for j in range(i,len(lst)+1) if sum(lst[i:j]) > n])
  return res[0] if res else -1

