
def lcm(n1, n2):
  num = max(n1,n2)
  while num%n1!=0 or num%n2!=0:
    num+=1
  return num

