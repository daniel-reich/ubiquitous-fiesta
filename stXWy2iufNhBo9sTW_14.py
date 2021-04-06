
def valid_rondo(s):
  return len(s) >= 3 and s.startswith('A') and s.endswith('A') and all([s[i]!=s[i+1] for i in range(len(s)-1)])

