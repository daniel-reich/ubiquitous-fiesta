
def compare_data(*args):
  if args==():
    return True
  else:
    a=type(args[0])
    return all(isinstance(x,a) for x in args)

