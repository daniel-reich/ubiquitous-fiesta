
def add(n1, n2):
  if any(not i for i in [n1, n2]):
    return 'Invalid Operation'
  
  return str(sum(map(int, [n1, n2])))

