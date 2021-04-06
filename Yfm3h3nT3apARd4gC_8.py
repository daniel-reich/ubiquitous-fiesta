
def rolls(lst):
  a = [lst[0]]
  for i in range(1,len(lst)):
    a.append(lst[i]*2 if lst[i-1]==6 else 0 if lst[i-1]==1 else lst[i])
  return sum(a)

