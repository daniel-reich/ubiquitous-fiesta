
def num_of_days(cost, savings, start):
  s = savings
  d = 0
  while s<cost:
    s+=start+(d%7)
    d+=1
    if d>=7 and d%7==0:
      start+=1
  return d

