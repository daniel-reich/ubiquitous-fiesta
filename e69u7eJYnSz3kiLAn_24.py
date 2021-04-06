
from hashlib import sha256
def hash_ops(lst):
  hash = sha256()
  for i in lst:
    hash.update(i.encode())
​
  alphas = ''.join(x for x in list(hash.hexdigest()) if x.isalpha())
  digits = ''.join(x for x in list(hash.hexdigest()) if x.isdigit())
​
  return sha256(alphas.encode() + digits.encode()).hexdigest()

