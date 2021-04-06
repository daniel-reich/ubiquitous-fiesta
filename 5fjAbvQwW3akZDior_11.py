
def unrepeated(txt):
  a=''
  for i in txt:
    if i not in a: a+=i
  return a

