
def tweet(txt):
  l=[i for i in txt.split() if i[0] in '@#']
  for i in range(len(l)):
    for j in ".,?!":
      l[i]=l[i].replace(j,'')
  return ' '.join(l)

