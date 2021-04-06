
def double_letters(w):
  t=0
  c=w[0]
  for l in w+' ':
    if c==l:
      t+=1
    else:
      if t==2:
        return True
      c=l
      t=1
  return False

