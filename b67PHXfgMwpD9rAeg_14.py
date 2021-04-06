
def plus_sign(txt):
  if txt[0].isalpha() or txt[len(txt) - 1].isalpha():
    return False
  
  for i in range(0, len(txt)):
    if txt[i].isalpha():
      previous = txt[i - 1]
      next = txt[i + 1]
      if previous != "+" or next != "+":
        return False
  
  return True

