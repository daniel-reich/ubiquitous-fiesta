
def isbn13(txt):
  if isValid10(txt):
    return to13(txt)
  elif isValid13(txt):
    return "Valid"
  else:
    return "Invalid"
  
  
  
def isValid10(txt):
  j = 10
  s = 0
  for i in txt:
    if i == 'X':
      s += 10 * j
    else:
      s += int(i)*j
    j -= 1
  return len(txt)==10 and s%11==0
​
def isValid13(txt):
  if 'X' in txt:
    return False
  j = [1,3,1,3,1,3,1,3,1,3,1,3,1]
  s=0
  for ind,val in enumerate(txt):
    s += j[ind]*int(val)
  return len(txt)==13 and s%10==0
​
def to13(txt):
  txt = '978'+txt[:-1]
  j = 1
  while not isValid13(txt+str(j)):
    j+=1
  return txt+str(j)

