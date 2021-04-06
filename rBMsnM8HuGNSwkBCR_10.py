
def add_bill(money):
  repl = money.replace('k','000')
  lst= repl.split(',')
  total = 0
  for x in lst:
    if x[0]== 'd':
      total+=int(x[1::])
​
  return total

