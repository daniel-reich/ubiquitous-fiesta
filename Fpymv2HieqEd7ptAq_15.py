
def split(txt):
  a = 0
  b = 0
  c = 0
  lst = []
  for i in txt:
    if i=='(' : a+=1
    elif i==')' : b+=1
    if a==b :
      lst.append(txt[c:c+a+b])
      c+=a +b 
      a = 0
      b = 0
  return lst

