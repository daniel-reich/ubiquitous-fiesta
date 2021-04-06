
def two_product(lst, n):
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if lst[i]*lst[j]==n:
        return sorted([lst[i],lst[j]])
  return None

