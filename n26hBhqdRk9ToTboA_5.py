
def nothing_is_nothing(*args):
  falsy=[0, {}, [], (), None, False]
  for i in args:
    if i in falsy:
      return False
  return True

