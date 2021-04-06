
def clean_up_list(lst):
  evens = []
  odds = []
  for e in lst:
    ee = int(e)
    if ee % 2 == 0:
      evens.append(ee)
    else:
      odds.append(ee)
  return [evens, odds]

