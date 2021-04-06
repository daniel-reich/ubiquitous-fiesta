
def plus_sign(txt):
  if len(txt) < 3:
    return False
  for i in range(1,len(txt) - 1):
    if ord(txt[i]) in range(97,123):
      print(txt[i])
      if txt[i-1] != '+' or txt[i+1] != '+':
        return False
  return True

