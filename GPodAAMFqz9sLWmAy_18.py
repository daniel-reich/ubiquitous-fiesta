
def one_odd_one_even(n):
  nlist = list(str(n))
  even = 0
  for x in nlist:
    if int(x) % 2 == 0:
      even+=1
    else:
      continue  
  if even == 1:
    return True
  else:
    return False

