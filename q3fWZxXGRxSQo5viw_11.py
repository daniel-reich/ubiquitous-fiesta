
def cal(length):
  res = length // 150 
  total = res * 30 + length 
  if length != 150:
    res = (total / 150) * 30 + (res * 10)
  else:
    return 30
  res = str(res).split('.')
  if res[-1] == '0':
    pass
  else:
    res[0] = int(res[0]) + 1
  return (int(res[0]))

