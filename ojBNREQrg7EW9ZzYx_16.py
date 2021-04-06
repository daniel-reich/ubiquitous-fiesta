
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  a = ['-','1','2','3','4','5','6','7','8','9','0']
  
  tot = ''
  total_money = list(total_money)
  for i in total_money:
    if i in a:
      tot += i
  cost = ''
  cost_of_one_chocolate = list(cost_of_one_chocolate)
  for i in cost_of_one_chocolate:
    if i in a:
      cost += i
  tot = int(tot)
  cost = int(cost)
  if tot < 1:
    return 'Invalid Input'
  elif cost < 1:
    return 'Invalid Input'
  ctr = tot // cost
  pur = tot // cost
  wrap = pur
  
  while wrap >= 3:
    pur = wrap // 3
    wrap = pur + wrap % 3
    ctr += pur
    
    
  return ctr

