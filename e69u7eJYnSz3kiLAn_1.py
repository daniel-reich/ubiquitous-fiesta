
import hashlib
def hash_ops(lst):
  encrypt = lambda x: hashlib.sha256(''.join(x).encode()).hexdigest()
  return encrypt(sorted(encrypt(lst), key = str.isdigit))

