
def happiness_number(s):
  h=0
  for i in range(len(s)-1):
    if s[i:i+2]==':)' or s[i:i+2]=='(:':
      h=h+1
    if s[i:i+2]==':(' or s[i:i+2]=='):':
      h=h-1
  return h

