
def is_apocalyptic(number):
  if str(2**number).count('666') == 1:
    return "Single"
  elif str(2**number).count('666') == 2:
    return "Double"
  elif str(2**number).count('666') == 3:
    return "Triple"
  elif str(2**number).count('666') == 0:
    return "Safe"
  else:
    return

