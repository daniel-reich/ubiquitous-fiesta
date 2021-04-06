
import re
def secret_password(message):
  if re.fullmatch(r'[a-z]{9}', message):
    p1,p2,p3=[message[i:i+3] for i in range(0,9,3)]
    p1=p1.replace(p1[0], str(ord(p1[0])-ord('a')+1)).replace(p1[2], str(ord(p1[2])-ord('a')+1))
    p2=p2[::-1]
    p3=''.join([chr(ord(x)+1) if x!='z' else 'a' for x in p3])
    return p2+p3+p1
  else:
    return "BANG! BANG! BANG!"

