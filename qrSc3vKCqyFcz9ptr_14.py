
def sum_round(num):
  num = str(num)
  num = num[::-1]
  o = []
  for i in range(len(num)):
    if num[i] != '0':
      o.append(str(int(num[i])*(10**i)))
  return ' '.join(o)

