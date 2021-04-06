
def neutralise(s1, s2):#It's like a chemichal reaction in some sort of way.
  lst = []
  for i in range(len(s1)):
    if s1[i] == '-' and s2[i] == '-':
      lst.append('-')
    elif s1[i] == '+' and s2[i] == '+':
      lst.append('+')
    else:
      lst.append('0')
  return "".join(lst)

