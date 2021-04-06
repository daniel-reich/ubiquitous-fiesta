
def make_happy(txt):
  for i in range(len(txt)):
    if txt[i] == '(':
      if txt[i-1] in [':', ';', '8', 'x']:
        txt = ''.join([txt[:i], ')', txt[i+1:]])
  return txt

