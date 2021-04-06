
def is_icecream_sandwich(txt):
  if txt == '':
    return False
  if len(set(txt)) == 1:
    return False
  firstchar = txt[0]
  while txt[0] == firstchar:
    if txt[0] != txt[-1]:
      print(txt)
      return False
      break
    txt = txt[1:-1]
  return len(set(txt))==1

