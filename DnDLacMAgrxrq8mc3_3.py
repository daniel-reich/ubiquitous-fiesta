
def blah_blah(t,n):
  s=t.split()
  return' '.join(s[:-n]+['blah']*(n,len(s))[n>len(s)])+'...'

