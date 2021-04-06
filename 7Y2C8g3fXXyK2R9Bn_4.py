
import string
def build_alphabet(key):
  alphabet = list(string.ascii_lowercase)
  if not key:
    return alphabet
  prefix = list()
  for k in key:
      if k not in set(prefix):
          prefix.append(k)
  
  return list(prefix) + [x for x in alphabet if x not in set(prefix)]
​
def keyword_cipher(key, message):
    alphabet = build_alphabet(key)
    alphabet_real = set(string.ascii_lowercase)
    return "".join([alphabet[(ord(c)%32)-1] if c in alphabet_real else c for c in message])

