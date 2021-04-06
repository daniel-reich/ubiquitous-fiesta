
def count_eatable_chocolates(total_money, cost_of_one_chocolate):
  
  money = ''
  for char in total_money:
    if char.isdigit() or char == '-': 
      money += char
  money = int(money)
  
  unit = ''
  for char in cost_of_one_chocolate:
    if char.isdigit() or char == '-':
      unit += char
  unit = int(unit) 
  if money <= 0 or unit <= 0: return ('Invalid Input')  
  eaten = money // unit
  rappers = eaten
​
  while rappers >= 3:
    eaten += rappers // 3
    rappers = rappers // 3 + rappers % 3
  return eaten

