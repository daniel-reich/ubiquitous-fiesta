
def compare_data(*args):
  return all(type(i)==type(j) for i,j in zip(args[:],args[1:]))

