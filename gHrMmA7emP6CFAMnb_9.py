
def is_apocalyptic(number):
  m = str(2**number).count(str(666))
  if m == 3:
    return "Triple"
  elif m == 2:
    return "Double"
  else: 
    return "Single" if m == 1 else "Safe"

