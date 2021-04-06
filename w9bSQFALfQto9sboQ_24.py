
def gcd(n1, n2):
  GCDArray = []
  if n1>n2:
    for GCD in range(n1):
      if GCD != 0 and n1 % GCD == 0 and n2 % GCD == 0:
        GCDArray.append(GCD)
  else:
    for GCD in range(n2):
      if GCD != 0 and n1 % GCD == 0 and n2 % GCD == 0:
        GCDArray.append(GCD)
  return GCDArray[len(GCDArray)-1]

