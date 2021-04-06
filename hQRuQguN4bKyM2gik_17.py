
def simple_check(a, b):
  check = lambda n1, n2: n1 % n2 == 0
  
  count = 0
  
  while 0 not in [a, b]:
    if check(max(a, b), min(a, b)) == True:
      count += 1
    a -= 1
    b -= 1
  
  return count

