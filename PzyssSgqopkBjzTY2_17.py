
def can_exit(lst):
  lst[0][0] = 'X'
  for a in range(0,len(lst)):
    l = lst[a]
    for b in range(len(l)):
      if (l[b] == 0 and l[b - 1] == 'X') or (lst[a-1][b] == 'X' and l[b] == 0):
        l[b] = 'X'
    lst[a] = l
  return True if lst[-1][-1] == 'X' else False

