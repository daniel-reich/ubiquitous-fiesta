
def is_it_inside(d, end, start):
  if start == end:
    return True
  for k,v in d.items():
    if end in v:
      return is_it_inside(d, k, start)
  else:
    return False

