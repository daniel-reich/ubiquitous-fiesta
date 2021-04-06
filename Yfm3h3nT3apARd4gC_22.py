
def rolls(lst):
  r=[lst[0]]
  for i in range(len(lst)-1):
    if lst[i]==1:
      r.append(0)
    elif lst[i]==6:
      r.append(lst[i+1]*2)
    else:
      r.append(lst[i+1])
  print(r)
  return sum(r)

