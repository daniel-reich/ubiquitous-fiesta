
def encrypt(key, message):
  
  cipher = []
  
  for i in range(0,len(key)-1,2):
    cipher.append(key[i:i+2])
    
  l = list(message)
  
  for i in range(0,len(l)):
    for j in range(0,len(cipher)):
      
      if cipher[j][0]==l[i]:
        l[i]=cipher[j][1]
        break
      elif cipher[j][1]==l[i]:
        l[i]=cipher[j][0]
        break
  return ''.join(l)

