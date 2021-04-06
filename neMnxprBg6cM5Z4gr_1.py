
def arithmetic_progression(start, diff, n):
  number = start
  s = ''
  for x in range(n):
    s+=str(number)+','+' '
    number += diff
    
    x+=1
  return s[0:len(s)-2]

