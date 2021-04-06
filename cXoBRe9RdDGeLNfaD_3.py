
def eight_bit(x):
  res = eval(x)
  x = x.split()
  x = [int(x[0]), x[1], int(x[2]), '=', res]
  for i in range(0,5,2):
    if not -128 <= x[i] < 128:
      return 'Overflow'
    if x[i] >= 0:
      x[i] = '{:b}'.format(x[i])
    else:
      x[i] = '1' + '{:07b}'.format(x[i]+128)
  return (res,' '.join(x))

