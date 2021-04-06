
def current_streak(today, lst):
  if len(lst) == 0: return 0
  if lst[-1].get('date') != today: return 0
  max = 0
  cnt = 0
  prev = 'none'
  for i in lst:
    if prev == 'none': 
      prev = i.get('date')[-2:]
      cnt = 1
    elif int(i.get('date')[-2:])-1 == int(prev):
      cnt += 1
      prev = i.get('date')[-2:]
    else:
      if cnt > max and prev == lst[-1].get('date'): max = cnt
      prev = i.get('date')[-2:]
      cnt = 1
  if cnt > max: max = cnt
  return max

