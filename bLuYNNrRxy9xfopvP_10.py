
def yahtzee_score_calc(lst):
​
  tot = 0
  for va in range(6):
    tot += lst[va].count(va+1)*(va+1)
  tot = (tot + 35) if (tot >= 63) else (tot)
​
  tempset = set()
​
  tempset = set(lst[6])
  for num in tempset:
    counts = lst[6].count(num)
    if counts >= 3:
      tot += sum(lst[6])
      break
​
  tempset = set(lst[7])
  for num in tempset:
    counts = lst[7].count(num)
    if counts >= 4:
      tot += sum(lst[7])
      break
      
  tempset = set(lst[8])
  if len(tempset) == 2:
    for num in tempset:
      if lst[7].count(num) == 3 or 2:
        tot += 25
        break
        
  lst[9].sort()
  co = lst[9][0]
  for va in range(4):
    if co != lst[9][va]:
      break
    co += 1
    if(va == 3):
      tot += 30
​
  lst[10].sort()
  co = lst[10][0]
  for va in range(5):
    if co != lst[10][va]:
      break
    co += 1
    if(va == 4):
      tot += 40
​
  tempset = set(lst[11])
  if len(tempset) == 1:
    tot += 50
​
  for num in lst[12]:
    tot+=num
​
  return tot

