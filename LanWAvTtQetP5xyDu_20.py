
def coins_div(lst):
  lst.sort()
  parts = [sum(lst)/3] * 3
  
  for i in range(3):
    while parts[i]:
      idx = next((idx for idx, coin in enumerate(lst) if coin == parts[i]), next((idx for idx, coin in enumerate(lst) if coin < parts[i]), -1))
      if idx < 0: return False
      else: parts[i] -= lst.pop(idx)
      
  return True

