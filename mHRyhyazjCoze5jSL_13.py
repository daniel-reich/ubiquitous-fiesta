
def double_swap(txt, c1, c2):
  res = []
  for char in txt:
    if char == c1:
      res.append(c2)
    elif char == c2:
      res.append(c1)
    else:
      res.append(char)
  return ''.join(res)

