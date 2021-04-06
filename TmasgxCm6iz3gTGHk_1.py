
def min_length(lst, n):
  a = len(lst)+1
  for i in range(len(lst)):
    for j in range(i+1,len(lst)+1):
      if sum(lst[i:j]) > n:
        a = min(len(lst[i:j]), a)
  return a if a <= len(lst) else -1

