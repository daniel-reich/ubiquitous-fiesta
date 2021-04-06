
def p13(txt):
  return sum(int(i) for i in txt[1::2])*3 + sum(int(i) for i in txt[::2])
def isbn13(txt):
  print (txt)
  l = len(txt)
  if l==10 or l==13:
    if l==10:
      if sum((10-i)*(10 if txt[i]=='X' else int(txt[i])) for i in range(10))%11==0:
        front = '978'+txt[:-1]
        return front + str(10-p13(front)%10)
    elif l==13:
      if p13(txt)%10==0:
        return 'Valid'
  return 'Invalid'

