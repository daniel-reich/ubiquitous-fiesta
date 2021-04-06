
def determineNatPosIdx(n):
  res=n
  rng=[10,100]
  digMul=1
  while n>rng[1]:
    res+=(rng[1]-rng[0])*digMul
    rng[0],rng[1]=10*rng[0],10*rng[1]
    digMul+=1
  return res+(n-rng[0])*digMul
  
def buildIdxLst(currPos,n):
  idxLst=[]
  for i in range(len(str(n))):
    idxLst.append(currPos+i)
  return idxLst
​
def is_early_bird(_range, n):
  res=[]
  s=''
  for i in range(_range+1):
    s+=str(i)
  natPosIdx=determineNatPosIdx(n)
  curIdx=-1
  try:
    while True:   
      curIdx=s.index(str(n),curIdx+1)
      res.append(buildIdxLst(curIdx,n))
      if natPosIdx==curIdx and 1==len(res): return res
  except ValueError:
    res.append("Early Bird!")
    return res

