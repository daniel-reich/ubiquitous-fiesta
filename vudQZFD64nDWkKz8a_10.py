
def grant_the_hint(txt):
  lst = []
  txt = txt.split()
  for i in range(max([len(i) for i in txt])+1):
    lst.append(' '.join([x[:i]+('_'*(len(x)-i)) for x in txt]))
  return lst

