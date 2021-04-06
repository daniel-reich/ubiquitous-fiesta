
def word_to_decimal(word):
  l = list(word)
  for i in range(len(l)):
    l[i] = l[i].lower()
  a = 0
  for i in range(len(l)):
    if ord(l[i]) > a:
      a = ord(l[i])
  b = 10 + a - 96
  myans = 0
  for i in range(len(l)):
    myans += (ord(l[i])-97+10)*b**((len(l))-i-1)
  return myans

