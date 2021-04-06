
def neutralise(s1, s2):
  return ''.join('0' if i.count('+') == 1 else i[0] for i in zip(s1, s2))

