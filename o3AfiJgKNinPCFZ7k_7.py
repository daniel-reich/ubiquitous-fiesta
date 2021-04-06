
def partition(txt, n):
  set=[]
  while len(txt)>n:
    set.append(txt[:n])
    txt=txt[n:]
  set.append(txt)
  return set

