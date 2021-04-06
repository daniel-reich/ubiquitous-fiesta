
def decrypt(s):
  A=[]
  i=0
  while i<len(s):
    if s[::-1][i]=='#':
      A.append(s[::-1][i+1:i+3])
      i+=3
    else:
      A.append(s[::-1][i])
      i+=1
  B=[x[::-1] for x in A][::-1]
  C=[int(x) for x in B]
  D=[chr(ord('a')+x-1) for x in C]
  return ''.join(D)

