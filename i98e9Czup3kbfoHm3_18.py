
def text_to_number_binary(txt):
  ret = []
  for w in txt.split():
    if w.lower() == 'zero':
      ret.append('0')
    if w.lower() == 'one':
      ret.append('1')
  if len(ret) < 8: return ""
  return ''.join(ret[:len(ret)-len(ret)%8])

