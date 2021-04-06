
def partition(txt, n):
  a=[]
  while len(txt)>n:
    a.append(txt[:n])
    txt=txt[n:]
  a.append(txt)
  return a

