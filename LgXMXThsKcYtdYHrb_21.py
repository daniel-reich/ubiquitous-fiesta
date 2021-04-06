
def split_and_delimit(txt, num, delimiter):
  i = 0
  s = []
  while i<len(txt):
    s.append(txt[i:i+num])
    if i+num<len(txt):
      s.append(delimiter)
    i = i+num
  return ''.join(s)

