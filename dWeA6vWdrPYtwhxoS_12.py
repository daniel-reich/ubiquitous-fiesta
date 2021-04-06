
def count_number(l):
  t = 0
  for i in l:
    if isinstance(i, list):
      t += count_number(i)
    elif isinstance(i, str):
      continue
    else:
      t += 1
  return t

