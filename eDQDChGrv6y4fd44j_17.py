
def can_put(txt, dim):
  count=0
  p=0
  for t in range(len(txt)):
    count+=1
    if t==len(txt)-1:
      p+=1
      if p>dim[1]:
        return False
      break
    elif txt[t]==" ":
      if p>dim[1]:
        return False
      p=0
    else:
      p+=1
  if count> dim[0]*dim[1]:
      return False
  return True

