
def same_length(txt):
  s = txt.replace('0',' ')
  d = [len(x) for x in  s.split()]
  return txt == ''.join('1'*x+'0'*x  for x in d)

