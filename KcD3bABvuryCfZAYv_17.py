
def most_frequent_char(lst):
  c=''.join(lst)
  res,x=[],0
  for i in set(c):
    if x < c.count(i):
      x=c.count(i)
      res = [i]
    elif x == c.count(i):
      res += [i]
  return sorted(res)

