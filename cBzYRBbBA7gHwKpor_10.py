
def secret_password(message):
  if(len(message)!=9):
    return "BANG! BANG! BANG!"
  for i in message:
    if(ord(i)<ord('a') or ord(i)>ord('z')):
      return "BANG! BANG! BANG!"
  a=message[0:3]
  b=message[3:6]
  c=message[6:]
  part1=str(ord(a[0])-ord('a')+1)+a[1]+str(ord(a[2])-ord('a')+1)
  part2=b[::-1]
  part3=''
  for i in c:
    if(ord(i)+1<=ord('z')):
      part3+=chr(ord(i)+1)
    else:
      part3+='a'
  return part2+part3+part1

