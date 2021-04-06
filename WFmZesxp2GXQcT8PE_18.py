
def digital_cipher(message, key):
  A=[ord(x)-ord('a')+1 for x in message]
  a, b=divmod(len(message), len(str(key)))
  nkey=str(key)*a+str(key)[:b]
  B=[int(x) for x in nkey]
  return [sum(x) for x in zip(A,B)]

