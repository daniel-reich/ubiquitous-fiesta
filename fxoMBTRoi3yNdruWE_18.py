
def in_box(lst):
  contador = 0
  for linha in lst:
    if "*" in linha:
      contador += 1
  if contador == 0:
    return False
  else:
    return True

