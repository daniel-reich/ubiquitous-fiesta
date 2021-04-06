
def binary_clock(time):
  res = []
  lst = [int(i) for i in time if i.isdigit()]
  for i in lst:
    res.append('{:04d}'.format(int(bin(i)[2:])))
  res = list(map(list,zip(*res)))
  
  res[0][0], res[0][2], res[0][4], res[1][0] = ' ', ' ', ' ', ' '
  return [''.join(i) for i in res]

