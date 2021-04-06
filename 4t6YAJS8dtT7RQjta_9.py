
def num_layers(n):
  result = 0.0005*2**n
  if n ==0:
    return '0.0005m'
  else:
    return str(result)+ "m"

