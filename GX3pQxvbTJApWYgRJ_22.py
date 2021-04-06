
def is_kaprekar(n):
  if n in [0,1]:
    return True
  test = str(n**2)
  if len(test) == 1:
    return False
  left = test[:len(test)//2]
  right = test[len(test)//2:]
  return int(left) + int(right) == n

