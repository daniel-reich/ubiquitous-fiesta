
def mirror_cipher(message, key="abcdefghijklmnopqrstuvwxyz"):
  out=""
  for i in message.lower():
    tmp=key.find(i)
    if tmp>-1:
      out+=key[-tmp-1]
    else:
      out+=i
  return out

