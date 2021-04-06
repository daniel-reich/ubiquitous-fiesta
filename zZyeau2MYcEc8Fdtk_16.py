
def round_number(num, n):
  r=num%n
  n1=num-r
  n2=n1+n
  if (num-n1)<(n2-num):
    return n1
  else:
    return n2

