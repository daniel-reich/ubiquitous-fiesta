
def letters_only(s):
  valor=False
  for i in s:
    if i.isdigit() or i.isupper():
      valor=False
      break
    else:
      valor=True
  return valor

