
import re
def scrambled(words, mask):
  p=''
  for x in mask:
    if x=='*':
      p+='.'
    else:
      p+=x
  
  A=[]
  for x in words:
    if bool(re.fullmatch(p,x)):
      A.append(x)
  return A

