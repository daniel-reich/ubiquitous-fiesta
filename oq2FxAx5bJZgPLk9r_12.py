
def sock_merchant(lst):
  d = {}
  for unit in lst:
    if unit in d:
      d[unit] +=1
    else:
      d[unit] = 1
  return sum([x//2 for x in d.values()])

