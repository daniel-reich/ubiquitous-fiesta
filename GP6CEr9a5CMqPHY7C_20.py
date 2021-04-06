
def words_to_sentence(words):
  newlist = []
  newlist2 = []
  if type(words) == type(None):
    return ''
  elif len(words) == 1:
    return words[0]
  elif len(words) == 0:
    return ''
  else:
    for eachword in words:
      if eachword == '':
        continue
      else:
        newlist2.append(eachword)
    x = ' '.join(newlist2)
    lasttwo = newlist2[-2:]
    lasttwo = ' and '.join(lasttwo)
    lasttwo = (lasttwo.lstrip(' ')).rstrip(' ')
    therest = newlist2[:-2]
    for eachword in therest:
      newlist.append(eachword + ',')
    x = ' '.join(newlist)
    return (('{} {}'.format(x,lasttwo)).lstrip(' ')).rstrip(' ')

