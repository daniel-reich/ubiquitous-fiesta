
def is_apocalyptic(number):
  num = 2 ** number
  count = str(num).count("666")
  if count == 0:
    return "Safe"
  elif count == 1:
    return "Single"
  elif count == 2:
    return "Double"
  elif count == 3:
    return "Triple"

