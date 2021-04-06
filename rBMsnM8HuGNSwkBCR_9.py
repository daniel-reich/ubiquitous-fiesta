
def add_bill(money):
  b =money.split(',')
  c = []
  for x in b:
    if x[0] == 'd':
      c.append(x[1:])
  y = 0
  for x in c:
    if x[-1] == 'k':
      y += int(x[:-1]) * 1000
    else:
      y += int(x)
  return y

