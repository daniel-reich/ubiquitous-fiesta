
def cap_to_front(s):
  x=''
  y=''
  for i in s:
    if i==i.upper():
      x+=i
    else:
      y+=i
  return x+y

