
def expanded_form(num):
  res = ''
  i = 0
  while num > 0:
    div = 10*10**i
    if num%div != 0:
      res = (str(num%div)+' + '+res) if res!='' else str(num%div)+res
      num -= num%div
    i += 1
  return res

