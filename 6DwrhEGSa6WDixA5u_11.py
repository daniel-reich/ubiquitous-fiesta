
def is_narcissistic(n):
  total = []
  for i in str(n):
    result = (int(i) ** len(str(n)))
    total.append(result)
    
  if sum(total) == n:
    return True
  else:
    return False

