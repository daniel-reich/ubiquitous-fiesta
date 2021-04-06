
def special_reverse(s, c):
  sentence = s.split(' ')
  s1 = []
  for i in sentence:
    if c in i:
      s1.append(i[::-1])
    else:
      s1.append(i)
  return ' '.join(s1)

