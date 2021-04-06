
def emphasise(txt):
  listtxt = txt.split(' ')
  caplist = []
  for word in listtxt:
      lowword = word.lower()
      capword = word.capitalize()
      caplist.append(capword)
  captxt = ' '.join(caplist)
  return captxt

