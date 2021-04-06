
def double_swap(txt, c1, c2):
  x=''
  for i in txt:
    if i==c1:
      x+=c2
    elif i==c2:
      x+=c1
    else:
      x+=i
  return x

