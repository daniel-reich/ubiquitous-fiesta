
def valid_rondo(s):
  return all([(s[i] == 'A' and s[-1] == 'A' and len(s)>2) for i in range(0, len(s), 2)])

