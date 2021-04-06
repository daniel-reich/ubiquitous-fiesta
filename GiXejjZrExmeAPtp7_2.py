
def fifth(*args):
  x = [i for i in args]
  if len(x) < 5:
    return "Not enough arguments"
  return type(x[4])

