
def show_the_love(lst):
  s = 0
  n = min(lst)
  m = min(lst)
  for i in lst:
    if i == n:
      continue
    else:
      lst[lst.index(i)] = round(3*i/4,2)
      s += round(i/4,2)
  n += s
  lst[lst.index(m)] = n
  return lst

