
def all_about_strings(txt):
  newlist = []
  newlist.append(len(txt))
  newlist.append(txt[0])
  newlist.append(txt[-1])
  if len(txt) % 2 != 0:
    middle = len(txt) // 2
    newlist.append(txt[middle])
  else:
    middle = len(txt) // 2
    to_add = txt[middle-1] + txt[middle]
    newlist.append(to_add)
  temp = txt[1]
  if txt.count(temp) == 1:
    newlist.append('not found')
    return newlist
  else:
    txt = txt[0:1] + '$' + txt[2:]
    first_index = txt.index(temp)
    newlist.append('@ index {}'.format(first_index))
    return newlist

