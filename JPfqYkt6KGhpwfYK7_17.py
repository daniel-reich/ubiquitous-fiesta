
def replace_the(txt):
  txt = txt.split()
  for i in range(len(txt)-1):
    if txt[i] == 'the':
      if txt[i+1][0] in 'aeiou':
        txt[i] = 'an'
      else:
        txt[i] = 'a'
  return ' '.join(txt)

