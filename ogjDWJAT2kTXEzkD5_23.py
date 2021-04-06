
def all_truthy(*args):
  for a in args:
    return True if bool(a) else False

