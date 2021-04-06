
def show_the_love(lst):
  m = min(lst)
  mi = lst.index(m)
  a = 0
  for i in range(len(lst)):
    if lst[i] != m:
      a += .25*lst[i]
      lst[i] = .75*lst[i]
  lst[mi] += a
  return lst

