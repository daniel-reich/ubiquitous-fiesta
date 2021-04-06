
def compare_data(*args):
  return all(map(lambda x: type(x[0]) == type(x[1]), zip(args, args[1:])))

