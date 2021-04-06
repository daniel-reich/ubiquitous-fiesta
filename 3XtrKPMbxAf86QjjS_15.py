
def same_case(txt):
  flag = txt[0].isupper()
  for i in range (1, len(txt)):
    if flag != txt[i].isupper():
      return False
  return True

