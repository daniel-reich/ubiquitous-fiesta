
def spin_around(lst):
  spin_total = 0
  for i in lst:
    if i =='right':
      spin_total += 90
    elif i =='left':
      spin_total -= 90
    else:
      continue
  return abs(int((spin_total/360)))

