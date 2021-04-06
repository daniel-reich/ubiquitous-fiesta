
def steps_to_convert(txt):
  l=0
  u=0
  for i in txt:
    if i.isupper():
      u+=1
    if i.islower():
      l+=1
  if l>u:
    return len(txt)-l
  elif u>l:
    return len(txt)-u
  else:
    return u

