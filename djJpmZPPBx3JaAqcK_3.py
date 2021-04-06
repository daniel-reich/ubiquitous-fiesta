
def maya_number(n):
  if n<1:return['@']
  m=['@']+[x+y for y in['','-','--','---']for x in['','o','oo','ooo','oooo']][1:]
  while n>0:m+=[m[n%20]];n//=20
  return m[20:][::-1]

