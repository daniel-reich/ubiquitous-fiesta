
def two_product(lst, n):
  for i in lst:
    for x in range(len(lst)-1):
      if i*lst[x]==n:
        return sorted([i,lst[x]])
  None

