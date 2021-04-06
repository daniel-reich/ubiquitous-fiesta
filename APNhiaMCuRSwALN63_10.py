
def almost_palindrome(txt):
  a=0
  for i in range(len(txt)//2):
    if txt[i] != txt[-i-1]:
      a+=1
  return(a==1)

