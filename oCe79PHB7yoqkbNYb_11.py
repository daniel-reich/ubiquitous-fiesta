
def break_point(n):
  n = str(n)
  for i in range(1, len(n)):
    left = sum(int(i) for i in n[i:])
    right = sum(int(i) for i in n[:i])
    if left == right:
      return True 
  return False

