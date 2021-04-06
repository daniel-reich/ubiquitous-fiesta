
def alternating_caps(txt):
  txt = txt.lower()
  res = ""
  i=0
  for ch in txt:
    if ch.isalpha():
      if i%2==0: res += ch.upper()
      else:      res += ch.lower()
      i+=1
    else:
      res += ch
  return res

