
def unstretch(w):
  s=''
  for x in range(1,len(w)):
    if w[x-1]!=w[x]:
      s+=w[x-1]
  return s+w[-1]

