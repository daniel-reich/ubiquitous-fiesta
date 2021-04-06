
def oddish_or_evenish(num):
  digits = [d for d in str(num)]
  sum = 0
  for d in digits:
    sum += int(d)
    
  if sum % 2 == 0:
    return "Evenish"
  else:
    return "Oddish"

