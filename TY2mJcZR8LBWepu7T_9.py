
def risiko(attacker, defender):
  att1=attacker
  dff1=defender
  l1=len(att1)
  l2=len(dff1)
  c=0
  att1.sort(reverse=True)
  print("att="+str(att1))
  dff1.sort(reverse=True)
  print("dff="+str(dff1))
  if l1>l2:
    l3=l2
  else:
    l3=l1
  for a in range(l3):
    if (att1[a]>dff1[a]):
      c=c+1
  return c

