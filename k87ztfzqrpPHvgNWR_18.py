
def widen_streets(lst, n):
  for i in range(len(lst)):
    if ' '*3 in lst[i]:
      lst[i]=lst[i].replace('   ', ' * ')
  for i in range(len(lst)):
    lst[i]=lst[i].replace(' ', ' '*n)
  for i in range(len(lst)):
    if '*' in lst[i]:
      lst[i]=lst[i].replace('*', ' ')
  return lst

