
def neutralise(s1, s2):
  l = len(s1)
  x = "" 
  for i in range(l): 
   if (s1[i] == '-' and s2[i]== '-'):
    x += '-'
   elif (s1[i] == '-' and s2[i]== '+') or (s1[i] == '+' and s2[i]== '-') :
    x += '0'
   elif (s1[i] == '+' and s2[i]== '+') :
    x += '+'
  return x

