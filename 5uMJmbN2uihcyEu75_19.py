
def weekly_salary(hours):
  sum1 = 0
  sum2 = 0
  a = 0
  ar1 = hours[:5]
  ar2 = hours[5:]
  for x in ar1:
    if x <= 8:
      sum1 += x*10
      x += 1
    else:
      a = x - 8
      sum1 += a * 15 + (x - a) * 10
      a = 0
      x += 1
  for y in ar2:
    if y <= 8:
      sum2 += y*20
      x += 1
    else:
      a = y - 8
      sum2 += a * 30 + (y - a) * 20
      a = 0
      y += 1
  return sum2 + sum1

