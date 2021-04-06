
def same(a1, a2):
  li1=[]
  li2=[]
  for i in a1:
    if i not in li1:
      li1.append(i)
  for x in a2:
    if x not in li2:
      li2.append(x)
  l1=len(li1)
  l2=len(li2)
  if l1==l2:
    return True
  else:
    return False

