
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  key2=[]
  for i in key:
    key2+=i
  ans=''
  for i in message:
    if i in key2:
      if key2.index(i)%2:ans+=key2[key2.index(i)-1]
      else:ans+=key2[key2.index(i)+1]
    else:ans+=i
  return ans

