
def de_nest(lst):
  result = None
  while lst:
    tmp = lst.pop()
    if not isinstance(tmp, list):
      result = tmp
    else:
      lst = tmp
  return result

