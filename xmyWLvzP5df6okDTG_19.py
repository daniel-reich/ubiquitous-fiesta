
def binary_to_decimal(binary):
  g=0
  for i in range(len(binary)-1,-1,-1):
    r=binary[len(binary)-i-1]*(2**i)
    g+=r
  return g

