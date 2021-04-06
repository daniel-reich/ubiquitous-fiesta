
def get_length(lst):
  t = 0
  if not lst: return 0
  for x in lst:
    if isinstance(x, list):
      t += get_length(x)
    else:
      t += 1
  return t

