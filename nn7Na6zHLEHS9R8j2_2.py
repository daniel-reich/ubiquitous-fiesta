
def deep_count(lst):
  ctr = 0
  while len(lst) > 0:
    if type(lst[0]) != list:
      ctr += 1
      del lst[0]
    else:
      for i in range(len(lst[0])):
        lst.append(lst[0][i])
      ctr += 1
      del lst[0]
    
  return ctr

