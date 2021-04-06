
def sum_round(num):
  res = []
  for idx, i in enumerate(reversed(str(num))):
    if i != '0':
      res.append(int(i) * 10**idx)
  return ' '.join(map(str, res))

