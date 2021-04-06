
def is_zygodrome(num):
  numStr = str(num)
  if num < 2:
    return False
  for i in range(0,len(numStr)):
    if i > 0:
      if numStr[i] == numStr[i-1]:
        continue
    if i < len(numStr) - 1:
      if numStr[i] == numStr[i+1]:
        continue
    return False
  return True

