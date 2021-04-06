
def plus_sign(txt):
  for i in range(1, len(txt) - 1, 2):
    if txt[i].isalpha():
      if txt[i-1] != '+' or txt[i+1] != '+':
        return False
  if txt[0].isalpha():
    return False
  return True

