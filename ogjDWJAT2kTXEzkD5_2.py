
def all_truthy(*args):
  for i in args:
    if bool(i) == False:
      return False
    else:
      return True

