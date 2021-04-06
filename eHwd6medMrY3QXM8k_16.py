
import re
def is_consecutive(s):
  for i in range(1, len(s)//2+1):
    p='\d'*i
    k=int(re.match(p, s).group())
    tex1=''
    tex2=''
    for x in range(len(s)//i):
      tex1+=str(k+x)
      tex2+=str(k-x)
      if s in tex1 or s in tex2:
        return True
  return False

