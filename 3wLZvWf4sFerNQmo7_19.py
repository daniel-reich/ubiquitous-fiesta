
def neutralise(s1, s2):
  lst = []
  for x,y in zip(s1,s2):
    if x != y: lst.append("0")
    else: lst.append(x)
  return "".join(lst)

