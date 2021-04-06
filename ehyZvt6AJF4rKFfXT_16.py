
def uncensor(txt, vowels):
  for i in vowels:
    txt = txt.replace('*', i, 1)
  return txt

