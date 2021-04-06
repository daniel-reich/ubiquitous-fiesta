
def compare_data(*args):
  return len(set(type(a) for a in args))<2

