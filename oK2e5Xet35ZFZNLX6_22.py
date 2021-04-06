
def neighboring(txt):
  for i in range(0,len(txt) - 1):
    if ord(txt[i]) + 1 != ord(txt[i+1]) and ord(txt[i]) - 1 != ord(txt[i+1]):
      return False
  return True

