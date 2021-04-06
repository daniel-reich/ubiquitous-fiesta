
def high_low(txt):
  lst = txt.split(' ')
  s = []
  for x in lst:
    s.append(int(x))
  s1 = sorted(s)
  s2 = ''
  s2 += str(s1[len(s1)-1])
  s2 += ' '
  s2 += str(s1[0])
  return s2

