
def blah_blah(s, n):
  s = s.split()
  return ' '.join(s[:-n] + min(n, len(s)) * ['blah']) + '...'

