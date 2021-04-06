
def is_icecream_sandwich(txt):
  if len(set(list(txt))) != 2 or len(txt)<2:
    return False   
  else:
    while len(set(list(txt))) == 2:
      if txt[0]==txt[-1]:
        txt = txt[1:-1]
      else:
        return False
    return len(set(list(txt))) == 1

