
def tweak_letters(txt, lst):
  alp = 'abcdefghijklmnopqrstuvwxyz'
  s = ''
  for i in range(len(txt)):
    s = s + alp[(alp.index(txt[i]) + lst[i]) % 26]
  return s

