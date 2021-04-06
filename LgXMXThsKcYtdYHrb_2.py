
def split_and_delimit(s, n, d):
  return d.join(s[i:i+n] for i in range(0, len(s), n))

