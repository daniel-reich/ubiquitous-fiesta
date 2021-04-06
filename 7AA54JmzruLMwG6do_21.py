
def is_icecream_sandwich(txt):
  if len(set(list(txt)))!=2: return False
  for i in range(len(txt)):
    if txt[i]!=txt[i+1]:
      sandwich=txt[:i+1]
      break
  if txt[-len(sandwich):]!=sandwich: return False
  return True

