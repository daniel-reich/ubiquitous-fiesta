
def add_bill(money):
  money_lst = money.split(',')
  sum = 0
  for den in money_lst:
    if 'd' in den:
      if den[-1] == 'k':
        sum+=int(den[1:-1])*1000
      else:
        sum+=int(den[1:])
  return sum

