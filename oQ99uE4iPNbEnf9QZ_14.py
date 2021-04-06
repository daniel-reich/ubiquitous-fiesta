
def no_perms_digits(n):
  sum_out= 1
  s = 0
  for i in range(n,0,-1):
    sum_out *= i 
  s = len(str(sum_out))
  return s

