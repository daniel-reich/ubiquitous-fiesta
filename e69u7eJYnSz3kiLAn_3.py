
from hashlib import sha256
def hash_ops(lst):
  h = list(sha256(''.join(lst).encode()).hexdigest())
  s = ''.join([c for c in h if c.isalpha()]+[c for c in h if c.isdigit()])
  return sha256(s.encode()).hexdigest()

