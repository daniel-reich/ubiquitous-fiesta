
def camelCasing(txt):
  x = (' '.join(txt.split('_'))).split(' ')
  newlist = []
  for i in range(len(x)):
    if i == 0:
      newlist.append(x[i].lower())
    else:
      newlist.append(x[i].capitalize())
  return ''.join(newlist)

