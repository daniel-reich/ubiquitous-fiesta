
def missing_num(lst):
  for n in range(1, 11):
    if n in lst:
      continue
    else:
      return n

