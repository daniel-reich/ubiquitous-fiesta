
def over_time(lst):
  start, finish, rate, mult = lst
  
  pay = 0
  if start < 17:
      pay += (min(17, finish) - start) * rate *1.00001
  if finish > 17:
      pay += (finish - max(17, start)) * rate * mult
      
  return '${:,.2f}'.format(pay)

