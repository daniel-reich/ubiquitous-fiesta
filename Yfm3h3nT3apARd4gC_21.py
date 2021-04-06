
def rolls(lst):
  return lst[0] + sum(0 if lst[i-1]==1 else 2*lst[i] if lst[i-1]==6 else lst[i] for i in range(1,len(lst)))

