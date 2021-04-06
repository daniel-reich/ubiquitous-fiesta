
def compare_data(*args):
  if len(args) == 0:
    return True
  types = [type(i) for i in args]
  return len(set(types)) == 1

