
def double_swap(txt, c1, c2):
  lista=[]
  for char in txt:
    if char==c1:
      lista.append(c2)
    elif char==c2:
      lista.append(c1)
    else:
      lista.append(char)
  return "".join(lista)

