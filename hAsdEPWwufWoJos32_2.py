
def no_yelling(phrase):
  x = phrase.split(' ')
  newlist = []
  for i in range(len(x)):
    if i == len(x)-1:
      y = list(x[i])
      if y[-1] == '!':
        y = list(''.join(y).replace('!',''))
        y.append('!')
        y = ''.join(y)
        print(y)
        newlist.append(y)
      elif y[-1] == '?':
        y = list(''.join(y).replace('?',''))
        y.append('?')
        y = ''.join(y)
        print(y)
        newlist.append(y)
      else:
        newlist.append(''.join(y))
    else:
      newlist.append(x[i])
  return ' '.join(newlist)

