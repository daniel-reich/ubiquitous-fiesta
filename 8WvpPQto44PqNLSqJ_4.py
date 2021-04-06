
def pad(msg):
  l = len(msg)
  if l == 140: return msg 
  o = (140-l-1)//2
  return  msg+'lo'* o +'l' if l%2 else  msg+' '+'lo'*o +'l'

