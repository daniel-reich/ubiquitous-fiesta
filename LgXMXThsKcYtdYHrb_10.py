
def split_and_delimit(txt, num, delimiter):
  a = []
  i = 0
  while i<len(txt):
   a.append(txt[0+i:i+num])
   i  +=  num
  return delimiter.join(a)

