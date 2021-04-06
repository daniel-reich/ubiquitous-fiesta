
def prime_divisors(num):
  if num == 1 or num == 0:
    return num
  div = []
  p_div = []
  t = 0
  for _ in range(2,num+1):
    if num % _ == 0:
      div.append(_)
  for var in div:
    for res in range(2,var+1):
      if var % res == 0:
        t = t + 1
    if t == 1:
      p_div.append(var)
      t = 0
    else:
      t = 0
  return p_div

