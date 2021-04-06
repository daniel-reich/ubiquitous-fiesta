
def keyboard_mistakes(txt):
  d = {'0' : 'O', '1' : 'I', '4' : 'A', '5' : 'S'}
  return ''.join(d[i] if i in d else i for i in txt)

