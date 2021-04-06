
def is_palindrome_possible(txt):
  k=set(txt)
  m=0
  for i in k:
    if((txt.count(i))%2!=0):
      m+=1
    if(m>1):
      return False
  return True

