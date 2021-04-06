
def lengthen(s1, s2):
  if len(s1) > len(s2):
    long = s1
    short = s2
  else:
    long = s2
    short = s1
  new = []
  for i in range(len(long)):
    new.append(short[i%len(short)])
  return ''.join(new)

