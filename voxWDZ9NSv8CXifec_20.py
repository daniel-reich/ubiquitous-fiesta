
def lemonade(bills):
  current_money = [0, 0]
  for bill in bills:
    if bill == 5:
      current_money[0] += 1
    elif bill == 10:
      current_money[0] -= 1
      if current_money[0] < 0: 
        return False
      current_money[1] += 1
    else:
      if current_money[0] > 2: 
        current_money[0] -= 3
      elif current_money[0] > 0 and current_money[1] > 0 : 
        current_money[0] -= 1; current_money[1] -= 1
      else:
        return False
​
  return True

