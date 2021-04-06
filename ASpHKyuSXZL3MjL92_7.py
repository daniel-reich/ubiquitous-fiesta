
def amplify(num):
  lst = list(range(1,num+1))
  newlst = []
  for i in lst:
    if i%4==0:
      newlst.append(i*10)
    else:
      newlst.append(i)
  return newlst

