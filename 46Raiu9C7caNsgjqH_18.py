
def compare_data(*args):
  return all(type(args[0])==type(i) for i in args)

