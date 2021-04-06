
def is_ladder_safe(n):
  gaps=list()
  for i in range(0,len(n)):
    if(len(n[i])<5):
      return False
    elif(n[i].count("#")==len(n[i])):
      gaps.append(i)
    elif(" " in n[i] and abs(n[i].count("#")-len(n[i]))!=len(n[i])-2):
      return False
  if(len(gaps)==0):
    return False
  z=gaps[1]-gaps[0]
  for i in range(1,len(gaps)):
    if(gaps[i]-gaps[i-1]>3 or (gaps[i]-gaps[i-1])!=z):
      return False
  return True

