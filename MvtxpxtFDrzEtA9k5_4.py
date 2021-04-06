
def palindrome_descendant(num):
  nam = str(num)
  if nam == nam[::-1]:
    return True
  if len(nam) < 3 or len(nam)%2 == 1:
    return False
  pairs = zip(nam[::2], nam[1::2])
  new_nam = ''.join([str(int(flip)+int(flop)) for flip,flop in pairs])
  print(new_nam)
  return palindrome_descendant(new_nam)

