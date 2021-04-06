
def oddish_or_evenish(num):
  num = str(num)
  sum1 = 0
  for i in num:
    sum1 +=  int(i)
  if sum1 %2 == 0:
    return "Evenish"
  else:
    return "Oddish"

