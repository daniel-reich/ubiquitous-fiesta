
def nothing_is_nothing(*args):
  for i in args:
    if i == None or i == False:
      return False
  return True

