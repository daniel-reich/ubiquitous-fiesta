
import hashlib
def hash_ops(lst):
  hash1 = hashlib.sha256()
  for string in lst:
    string = bytes(string,'utf-8')
    hash1.update(string)
  string = hash1.hexdigest()
  string = "".join([char for char in string if char in "abcdef"]) + "".join([char for char in string if char in "0123456789"])
  return hashlib.sha256(bytes(string,'utf-8')).hexdigest()

