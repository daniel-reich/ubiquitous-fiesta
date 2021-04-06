
def magic(txt):
  l=[int(x) for x in txt.split(' ')]
  return str(l[0]*l[1]) in str(l[2])[1:]

