
def shared_letters(txt1, txt2):
  a=[]
  for i in set(txt1):
    for e in set(txt2):
      if e==i:
        a.append(e)
  return len(a)

