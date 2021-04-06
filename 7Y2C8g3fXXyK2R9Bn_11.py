
from string import ascii_lowercase as al
def keyword_cipher(key, message):
  cipher = sorted(al,key=lambda x:(key+al).index(x))
  dic = dict(zip(al,cipher))
  return ''.join(dic[c] if c.isalpha() else c for c in message)

