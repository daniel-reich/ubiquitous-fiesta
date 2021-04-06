
def double_swap(txt, c1, c2):
  a = ''
  for i in txt:
    if i == c1:
      a += c2
    elif i == c2:
      a += c1
    else:
      a += i
  return a

