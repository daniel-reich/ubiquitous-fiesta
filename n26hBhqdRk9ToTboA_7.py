
def nothing_is_nothing(*args):
  ans = True
  for x in args:
    if not x:
      ans = False
      break
  return ans

