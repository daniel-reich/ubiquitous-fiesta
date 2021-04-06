
def num_layers(n):
  if n == 0:
    return "{}m".format(0.0005)
  return "{}m".format(0.0005 * 2**float(n))

