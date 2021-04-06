
def cleave(s,l):
  r,l='',sorted(l)[::-1]
  while s:
    f=1
    for w in l:
      if s[:len(w)]==w:r,s,f=r+' '+w,s[len(w):],0
    if f:return'Cleaving stalled: Word not found'
  return r[1:]

