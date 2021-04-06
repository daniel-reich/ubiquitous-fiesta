
def is_kaprekar(n):
  key = n * n
  if len(str(key)) == 1:
    left = 0
    right = key
    
  else:
    length = len(str(key))
    left = str(key)[:length//2]
    right = str(key)[length//2:]
  
  #print(left, right)
  if n == int(left) + int(right):
    return True
  else:
    return False

