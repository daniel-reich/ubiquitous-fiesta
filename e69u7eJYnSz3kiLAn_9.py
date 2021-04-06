
def hash_ops(lst):
  import hashlib
  text = ''.join(lst)
  t = hashlib.sha256(text.encode()).hexdigest()
  a = ''.join([t[x] for x in range(len(t)) if t[x].isalpha()])
  n = ''.join(str(i) for i in [int(t[x]) for x in range(len(t)) if t[x].isnumeric()])
  T = a+n
  return hashlib.sha256(T.encode()).hexdigest()

