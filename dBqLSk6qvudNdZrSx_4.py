
def is_boiling(temp):
  if temp.count('F'):
    return float(temp.strip('F')) >= 212
  else:
    return float(temp.strip('C')) >= 100

