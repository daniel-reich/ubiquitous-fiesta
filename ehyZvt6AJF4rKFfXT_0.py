
def uncensor(txt, vowels):
  txt = txt.replace('*', '{}')
  return txt.format(*vowels)

