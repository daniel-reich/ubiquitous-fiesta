
def will_fit(cargo, x):
  
  total = 0
​
  for i in cargo:
    if i == 'M':
      total += 100
    elif i == 'L':
      total += 200
    else:
      total += 50
​
  return(total >= sum(x))

