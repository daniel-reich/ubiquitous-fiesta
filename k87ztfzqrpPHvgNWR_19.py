
def widen_streets(lst, n):
  end = list(lst[-1])
  indexes = [i for i in range(len(end)) if end[i]==' ']
  for i in range(len(lst)):
    lst[i] = list(lst[i])
    for j in indexes:
      lst[i][j] = ' '*n
    lst[i] = ''.join(lst[i])
  return lst

