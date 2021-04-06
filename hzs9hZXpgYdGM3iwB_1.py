
def alternating_caps(txt):
  b,c='',0
  for i in txt:
      if i==' ':
        b+=' '
        continue
      elif c%2==0:
        b+=i.upper()
        c+=1
      else:
        b+=i.lower()
        c+=1
  return b

