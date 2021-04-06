
def validate_swaps(lst, txt):
  l=[]
  c=0
  for i in lst:
    if len(i)>len(txt):
      l.append(False)
    else:
      for j in range(0,len(i)):
        if i[j] == txt[j]:
          c=c+1
      if c == len(txt)-2:
        l.append(True)
        c=0
      else:
        l.append(False)
        c=0
  return l

