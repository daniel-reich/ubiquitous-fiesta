
from string import ascii_lowercase
def mirror_cipher(message,key=ascii_lowercase):
  dic = dict(zip(key,key[::-1]))
  return ''.join(dic[c] if c in dic else c for c in message.lower())

