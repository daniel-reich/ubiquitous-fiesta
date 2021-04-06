
import hashlib
def hash_ops(lst):
  h = hashlib.sha256()
  for s in lst:
    h.update(s.encode())
  return hashlib.sha256(''.join(sorted(h.hexdigest(), key=str.isdigit)).encode()).hexdigest()

