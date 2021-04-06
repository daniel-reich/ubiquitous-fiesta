
def ABA(s):
  left = ''
  right = ''
  middle = ''
  for x in range(65, ord(s)+1):
    left = left+middle+right
    right = left
    middle = chr(x)
  return left + middle + right

