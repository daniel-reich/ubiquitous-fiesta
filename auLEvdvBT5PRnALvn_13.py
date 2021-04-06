
def mirror_cipher(message, key='abcdefghijklmnopqrstuvwxyz'):
  newmsg = ''
  for x in message.lower():
    if key.__contains__(x):
      newmsg += key[-(key.index(x) + 1)]
    else: newmsg += x
  return newmsg

