
from hashlib import sha256
​
def hash_ops(lst):
  return sha256(''.join(sorted(sha256(''.join(lst).encode()).hexdigest(), key=lambda x:x.isnumeric()*200)).encode()).hexdigest()

