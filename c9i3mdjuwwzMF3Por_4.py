
def isprime(n):
  for i in range(n):
    if i<2:
      continue
    if n%i==0:
      return False
      break
  else:
    return True
    
def isbemirp(n):
  lst=','.join(str(n)).split(',')
  ls=[]
  for i in lst:
    if i=='6':
      ls.append('9')
    elif i=='9':
      ls.append('6')
    else:
      ls.append(i)
  num=int(''.join(ls))
  if isprime(num) and isprime(int(str(num)[::-1])):
    return True
  else:
    False
    
def bemirp(n):
  if not isprime(n):
    return 'C'
  else:
    if str(n)==str(n)[::-1]:
      return 'P'
    elif not isprime(int(str(n)[::-1])):
      return 'P'
    elif isbemirp(n):
      return 'B'
    else:
      return 'E'

