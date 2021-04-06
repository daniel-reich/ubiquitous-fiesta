
def bonus(days):
  a,b,c = 0,0,0
  if days <= 32: pass
  elif days >= 33 and days < 41:
    a = days - 32
  elif days <= 48:
    a,b = 8, days - 41
  else:
    a,b,c = 8,8,days -48
  return a*325 + b*550 + c*600

