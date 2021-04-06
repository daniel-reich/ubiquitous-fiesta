
def lcm(n1, n2):
  if (n1 > n2):
    gre = n1
  else:
    gre = n2
  while (True):
    if ((gre % n1 == 0) and (gre % n2 == 0)):
     lcm = gre
     break
    gre += 1
  return lcm

