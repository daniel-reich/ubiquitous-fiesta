
def is_prime(num):
  nbin = bin(num-1)[2:][::-1]
  for i in [2,3,5,7,11,13,17,19,23,29]:
    power = i
    test = 1
    for k in range(len(nbin)):
      test = test*power % num if int(nbin[k])==1 else test
      power = power**2 %num
    if test!=1: return False
  return True

