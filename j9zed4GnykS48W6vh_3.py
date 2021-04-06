
def digits(num):
  s = 0
  k = 1
  occ = 9
  n = 10
  while num >= n:
    s += k*occ
    k += 1
    occ *= 10
    n *= 10
  return s + (num-n//10)*k

