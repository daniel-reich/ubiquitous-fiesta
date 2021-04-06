
import hashlib 
def hash_ops(lst):
  lst1 = sorted(list(hashlib.sha256(''.join(lst).encode('utf-8')).hexdigest()),key=str.isdigit)
  new_hash = hashlib.sha256(''.join(lst1).encode('utf-8')).hexdigest()
  return new_hash

