
def tweak_letters(txt, lst):
  
  a = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
  
  indexes = []
  
  for l8r in txt:
    for n in range(0, 26):
      tl8r = a[n]
      if tl8r == l8r:
        indexes.append(n)
        break
  
  ns = ''
  for n in range(0, len(indexes)):
    index = indexes[n]
    dif = lst[n]
    
    nindex = index + dif
    while nindex >= 26:
      nindex -= 26
    nl8r = a[nindex]
    ns += nl8r
  
  return ns

