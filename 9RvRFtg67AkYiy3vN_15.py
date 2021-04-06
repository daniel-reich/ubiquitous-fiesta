
def left_rotations(str1):
  lk=[]
  lk.append(str1)
  for i in range(1,len(str1)):
    lk.append(str1[i:]+str1[:i])
  return lk
def right_rotations(txt):
  rk=[]
  vr=left_rotations(txt)
  fst=vr[0]
  rk.append(fst)
  rk.extend(vr[::-1][:-1])
  return rk

