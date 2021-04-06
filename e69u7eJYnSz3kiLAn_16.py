
def hash_ops(lst):
  import hashlib
  first_hash = hashlib.sha256()
  for st in lst:
      first_hash.update(st.encode())
  new_str = ''.join(sorted(first_hash.hexdigest(), key=str.isdigit )).encode()
  return hashlib.sha256(new_str).hexdigest()

