
def absolute(txt):
  if 'a' not in txt.lower().split(' '):
    return txt
  else:
    x = txt.split(' ')
    newlist = []
    for eachword in x:
      if eachword == 'a':
        newlist.append('an absolute')
      elif eachword == 'A':
        newlist.append('An absolute')
      else:
        newlist.append(eachword)
    return ' '.join(newlist)

