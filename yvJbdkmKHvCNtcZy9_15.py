
def is_disarium(n):
  total = 0
  for i in range(1,len(str(n))+1):
    total += int(str(n)[i-1]) ** i
    
  if total == n:
    return True
  return False

