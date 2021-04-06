
def simple_pair(lst, n):
  for i in range(len(lst)-1):
    for j in lst[i+1:]:
      if lst[i]*j==n:return [lst[i],j]

