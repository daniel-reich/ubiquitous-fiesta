
def digital_cipher(message, key):
​
  #message,key= "mubashir", 1990
​
  key=list(str(key))
  key=list(map(int,key))
  r_key=len(message)//len(key)
  t_key=key+key*r_key+(key[:len(message)-len(key)] if len(message)%len(key) else [])
 
  return [sum(i) for i in list(zip([ord(i)-96 for i in message],t_key))]
​
def digitalCipher(msg,key):
  return digital_cipher(msg,key)

