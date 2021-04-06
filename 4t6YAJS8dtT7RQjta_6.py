
def num_layers(n):
  if n > 0:
    return str(0.0005*(2 ** n)) + 'm'
  else:
    return '0.0005m'

