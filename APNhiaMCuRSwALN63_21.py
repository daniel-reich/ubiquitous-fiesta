
def almost_palindrome(txt):
  k=0
  for i in range(int(len(txt)/2)):
    if txt[i]!=txt[-i-1]:
      k+=1
  if k==1:
    return True
  return False

