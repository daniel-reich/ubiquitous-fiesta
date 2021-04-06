
def mirror_cipher(message, key='abcdefghijklmnopqrstuvwxyz'):
  message=message.lower()
  res=''
  for x in message:
    if x in key:
      res+=key[len(key)-key.find(x)-1]
    else:
      res+=x
  return res

