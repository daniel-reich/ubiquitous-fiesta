
def secret(num):
  s=[int(x) for x in str(num)]
  A=[]
  for x in s:
    if x%2:
      A.append(1)
    else:
      A.append(0)
  if A==[1,1]:
    return s[0]-s[1]
  elif A==[0,0]:
    return s[0]*s[1]
  else:
    return s[0]**s[1]-s[0]*s[1]

