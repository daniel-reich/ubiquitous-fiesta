
import re
import hashlib
def hash_ops(lst):
  hashed = hashlib.sha256()
  for w in lst:
    hashed.update(w.encode())
  hashed = hashed.hexdigest()
  bla = "".join(re.findall(r"[a-z]+",hashed)) + "".join(re.findall(r"\d+",hashed))
  return hashlib.sha256(bla.encode()).hexdigest()

