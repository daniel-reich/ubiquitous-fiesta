
def monkey_talk(txt):
  l = txt.split(' ')
  myans = []
  v = ['a','e','i','o','u']
  for i in range(len(l)):
    if l[i][0].lower() in v:
      if i > 0:
        myans.append('eek')
      else:
        myans.append('Eek')
    else:
      if i > 0:
        myans.append('ook')
      else:
        myans.append('Ook')
  return ' '.join(myans)+'.'

