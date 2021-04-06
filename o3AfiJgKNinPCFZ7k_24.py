
def partition(txt, n):
  return [txt[n*x:n*x+n] for x in range(0,len(txt)//n)]+\
  ([txt[len(txt)-len(txt)%n:]] if len(txt)%n else [])

