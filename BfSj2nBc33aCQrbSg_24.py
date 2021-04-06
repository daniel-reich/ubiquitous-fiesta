
def truncatable(n):
  l = n
  r = n
  left = True
  right = True
  for i in range(2,n//2):
    if n % i == 0:
      return False
  for i in str(n):
    if i == "0":
      return False
      
      
  while len(str(l)) > 1:
    l = int(str(l)[1:])
    for i in range (2,l//2+1):
      if l%i == 0:
        left = False
  if l == 1:
    left = False
      
      
  while len(str(r)) > 1:
    r = int(str(r)[:-1])
    for i in range (2,r//2+1):
      if r%i == 0:
        right = False
  if r == 1:
    right = False
        
        
        
  if left and right:
    return "both"
  if left:
    return "left"
  if right:
    return "right"
  if not left and not right:
    return False

