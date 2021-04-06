
def valid_rondo(s):
  return len(s) > 2 and s[0] == s[-1] == 'A' and all(i * 2 not in s for i in s)

