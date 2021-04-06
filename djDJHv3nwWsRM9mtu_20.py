
import re
def validate_spelling(txt):
  txt.replace(' ','')
  print(txt)
  words = txt.split('. ')
  print(words)
  w = ''.join(words[0:(len(words)-1)])
  w = w.title()
  t = re.compile('[,\.!?]')
  out = t.sub('',words[-1])
  print(w)
  print(t)
  return w==out

