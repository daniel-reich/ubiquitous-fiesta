
def compare_data(*args):
  return all(type(x) == type(args[0]) for x in args)

