
def steps_to_convert(txt):
  x=0
  y=0
  for i in txt:
    if i.isupper():
      x+=1
    else:
      y+=1
  if x>y:
    return y
  else:
    return x

