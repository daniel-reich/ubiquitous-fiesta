
def numberSequence(n):
  if n < 1:
    return '-1'
  if n == 1:
    return '1'
    
  m = n//2 if not n%2 else n//2 + 1
  end = [i for i in range(1,m+1)]
  beg = end[::-1] if not n%2 else end[:0:-1]
  return ' '.join(str(i) for i in beg+end)

