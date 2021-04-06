
def is_apocalyptic(number):
  num = str(2 ** number)
  occurrences = num.count("666")
  if occurrences == 0:
    return "Safe"
  elif occurrences == 1:
    return "Single"
  elif occurrences == 2:
    return "Double"
  elif occurrences == 3:
    return "Triple"

