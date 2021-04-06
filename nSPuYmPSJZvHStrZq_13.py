
def oddeven(lst):
  odds = 0
  evens = 0
  for i in lst:
    if int(i) % 2 == 0:
      evens +=1
    else:
      odds +=1
  return odds > evens

