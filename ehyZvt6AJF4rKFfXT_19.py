
def uncensor(txt, vowels):
  for n in range(0,txt.count('*')):
    txt = txt.replace('*', vowels[n], 1)
  return txt

