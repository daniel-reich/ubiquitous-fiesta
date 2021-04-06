
def blah_blah(txt, n):
  txt = txt.split()[::-1]
  for i in range(n):
    if i > len(txt)-1:
      break
    txt[i] = 'blah'
  return ' '.join(txt[::-1])+'...'

