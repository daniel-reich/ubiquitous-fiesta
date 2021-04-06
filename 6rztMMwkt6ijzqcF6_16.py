
def is_repeated(strn):
  for i in range(1, len(strn) // 2 + 1):
    if strn.count(strn[0:i]) == len(strn) / i:
      return len(strn) / i
  return False

