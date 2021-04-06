
def text_to_number_binary(txt):
  txt = txt.lower()
  new = []
  r_di = {'zero': '0', 'one': '1'}
  for x in txt.split():
    if x  in r_di.keys():
      new.append(x)
  txt = ''.join(new)
  txt = txt.replace('zero', '0')
  txt = txt.replace('one', '1')
  over_h = len(txt) % 8
  return txt[0:len(txt)-over_h]

