
def nothing_is_nothing(*args):
  for i in args:
    if not i:
      return False
  return True

