
def available_spots(lst, num):
  spots = 0
  
  if num % 2 == 0:
    for i in range(len(lst) - 1):
      if lst[i] % 2 != 0 and lst[i+1] % 2 != 0:
        continue
      else:
        spots += 1
  else:
    for i in range(len(lst) - 1):
      if lst[i] % 2 == 0 and lst[i+1] % 2 == 0:
        continue
      else:
        spots += 1
​
  return spots

